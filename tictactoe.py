#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tictactoe.py
#  
#  Copyright 2021 culpd <culpd@PERTTL075>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import time 
		
def print_board(board):
	pos = 1
	for row_num, row in enumerate(board):
		for col_num, col in enumerate(row):
			if col == -15:
				print (pos," ",end = '')
			
			elif col == 3:
				print ("X"," ",end = '')
			else:
				print("O"," ",end = '')
			pos+=1
		print("")
	print("")
			

def make_move(board, current_player):
	move = -1
	while move == -1:
		print_board(board)
		print("Player number ",current_player+1,"(",player_token[current_player],")"," it is your move.")
		move = input("What position do you want to place your token? ")
		move = int(move)
		if move>9 or move<1:
			print("That is not a legal move!")
			move = -1
			continue
		row = (move-1)//3
		col = (move%3) - 1
		if board[row][col] == -15:
			board[row][col] = player_value[current_player]
		else:
			print("That is not a legal move!")
			move = -1
			continue

		
def check_draw(board):
	draw = 0
	for row in board:
		if -15 not in row:
			draw += 1
	if draw == 3:
		return True
	else:
		return False

def do_game_won():
	for x in range(15):
		print(x*" ","Player number",current_player+1," wins!!!")
		time.sleep(.05)
	for x in range(14,-1, -1):
		print(x*" ","Player number",current_player+1," wins!!!")
		time.sleep(.05)
			
def check_game_won(board):
	#first check the rows
	for row in board:
		#print ("checking row:", row)
		total = sum(row)
		if total == 15 or total == 9:
			return True
	#next check the columns
	for col in range(3):
		#print ("checking col:", col)
		total = board[0][col] + board[1][col] + board[2][col]
		if total == 15 or total == 9:
			return True
			
	#check diagonals
	total = board[0][0] + board[1][1] + board[2][2]
	if total == 15 or total == 9:
		return True
	total = board[0][2] + board[1][1] + board[2][0]
	if total == 15 or total ==9:
		return True
	return False
			
def swap_players(current_player):
	if current_player == 0:
		current_player = 1
	else:
		current_player = 0
	return current_player
		
current_player = 0
player_token=["X","O"]
player_value = [3,5]


board = [ [-15 for i in range(3)] for j in range(3) ]
"""
board = [ 
			[-15,-15,-15],
			[-15,-15,-15],
			[-15,-15,-15]
		]
"""

def main(args):
	global current_player
	while True:
		make_move(board, current_player)
		won = check_game_won(board)
		if won:
			do_game_won()
			break
		draw=check_draw(board)
		if draw:
			print("The game ends in a draw!")
			break
		current_player = swap_players(current_player)
		
		



if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
