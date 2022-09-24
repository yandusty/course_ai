from random import randint
#보드생성 
class tic:
    def __init__(self):
        self.board = [' ',' ',' '
                    ,' ',' ',' '
                    ,' ',' ',' ']
        self.order = 0
        self.playtype = ''
        self.computertype = ''
        self.win =''
        
    def ordering(self): #순서 정하기
        ans = input("first? y / n\n")
        while(1):
            if ans.lower() == 'y':
                self.order = 1
                return self.order
            elif ans.lower() =='n':
                self.order = 2
                return self.order
            else:
                print("please input correct answer\n")
                ans = input("first? y / n\n")
            
            
    def x_or_o(self): #x o정하기
        ans = input("X or O? \n")
        while(1):
            if ans.lower() =='x' or ans.lower() =='o':
                self.playtype = ans
                self.computertype = 'O' if self.playtype.lower() =='x' else 'X'
                return self.playtype
            else:
                print("please input correct answer\n")
                ans = input("X or O? \n")
                
    def prepare_game(self): #게임준비 (초기화?)
        self.ordering()
        self.x_or_o()
        self.board = [' ',' ',' '
                    ,' ',' ',' '
                    ,' ',' ',' ']
        
    def judge_win(self): #누가 이겼는지 판별
        temp = self.board
        for i in range(3):
            if temp[i*3]== temp[i*3+1]== temp[i*3+2]: #x축 확인
                if temp[i*3] == self.playtype:
                    self.win = 'player win'
                    return self.win
                elif temp[i*3] == self.computertype:
                    self.win = 'computer win'
                    return self.win
            if temp[i]== temp[i+3] == temp[i+6]: #y축 확인
                if temp[i] == self.playtype:
                    self.win = 'player win'
                    return self.win
                elif temp[i] == self.computertype:
                    self.win = 'computer win'
                    return self.win
        if temp[0] == temp[4]== temp[8] or temp[2]==temp[4]==temp[6]:#대각선 확인
            if temp[4] == self.playtype:
                self.win = 'player win'
                return self.win
            else:
                self.win = 'computer win'
                return self.win
        elif ' ' not in temp: #그외의 조건은 비김
            self.win = 'draw'
            return self.win
    
    def com_abs(self): #비기기위한 첫수 혹은 두번째 수
        temp = self.board
        if self.order == 1:
            if temp[4] == self.playtype:
                if temp[0] == ' ':
                    temp[0] = self.computertype
            else:
                temp[4] = self.computertype
        else:
            temp[4] = self.computertype
        return self.board    
       
    
    def play_game_com(self): #컴퓨터는 플레이어의 승리를 최대한 막는조건
        temp = self.board
        for i in range(3):
            if temp[i*3:i*3+3].count(self.playtype)==2: #플레이어의 것이 2개이상있는지 x축 탐색
                if self.computertype not in temp[i*3:i*3+3]:#그안에 자신의 것이 있는지 확인
                    for j in range(3):
                        if temp[i*3+j]==' ':
                            temp[i*3+j] = self.computertype
                            return self.board
            
            elif temp[i::3].count(self.playtype) == 2: #플레이어의 것이 2개이상 있는지 y축 탐색
                if self.computertype not in temp[i::3]:#그안에 자신의 것이 있는지 확인
                    for j in range(3):
                        if temp[i+j*3]==' ':
                            temp[i+j*3] = self.computertype
                            return self.board
        if temp[6] == ' ':
            temp[6] = self.computertype
            return self.board
        elif temp[2]== ' ':
            temp[2] = self.computertype
            return self.board
        else:
            for i in range(9):
                if temp[i] == ' ':
                    temp[i] = self.computertype
                    return self.board
                
        
    def play_game_player(self): #플레이어가 1부터 9를 입력하고 그에따라 판별후 배치
        temp = self.board
        pos = int(input("enter 1 to 9 pos you to want \n"))
        while(1):
            if pos <10 and pos>0:
                if temp[pos-1] == ' ':
                    temp[pos-1] = self.playtype
                    return self.board
                elif ' ' not in self.board:
                    return self.board
                else:
                    pos = int(input("please enter the correct number or position"))
            else:
                pos = int(input("please enter the correct number or position"))
                
    def print_board(self):
        temp = self.board
        for i in range(3):
            print('-----')
            print(temp[i*3],temp[i*3+1],temp[i*3+2],sep = '|',end = "\n")
            
    def start_game(self):
        self.prepare_game()
        if self.order == 1: #플레이어먼저시작
            self.play_game_player()
            self.print_board()
            self.com_abs()
            self.print_board()
            while(' 'in self.board and self.win ==''):
                self.play_game_player()
                self.print_board()
                self.play_game_com()
                self.print_board()
                self.judge_win()
        else:#컴퓨터먼저시작
            self.com_abs()
            self.play_game_player()
            while(' 'in self.board and self.win ==''):
                self.play_game_com()
                self.play_game_player()
                self.print_board()
                self.judge_win()
        print(self.win)
        
game = tic()
game.start_game()
