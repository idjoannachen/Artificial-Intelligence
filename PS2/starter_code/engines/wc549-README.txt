In this homework, we implemented minimax search and alpha-beta pruning minimax search. The heuristic function is from [1]. It returns an integer specifying the attractiveness of a potential move. The greater the number, the more attractive a given move is. The number is evaluated through piece count, legal moves count, and corner occupancy. In the experiment, we run the minimax player and alpha-beta minimax player against the player greedy and random1, random2, random3 with depth = 2, 3, 4. The results including the total number of nodes generated per round, the total number of duplicate nodes per round, average branching factors, and runtime per round, are shown in Table 1-8. The results show that the alpha-beta minimax search is better than the vanilla minimax search. 

Table 1: Minimax Search vs. Greedy Results (python3 othello.py student greedy)
					Depth = 2			Depth = 3			Depth = 4
Total # of nodes generated per round 	66.0				366.1875			6348.875
Total # of duplicate nodes per round 	54.29032258064516		322.875				5728.875
Average branching factors 		6.162650602409639		8.491304347826087		9.572370900866943
Runtime per round 			0.10727241731459095		0.376998133957386		4.740004003047943
Score (student vs. greedy)		53 vs. 11			59 vs. 5			N/A
Remaining time (student vs. greedy)	26.999999999999983 vs. 30.0	17.7 vs. 30.0			N/A
Results					student wins			student wins			student ran out of time
run 10 times, student wins #		10/10				10/10				student ran out of time 

Table 2: Alpha-beta Pruning Minimax Search vs. Greedy Results (python3 othello.py student greedy -aB)

					Depth = 2			Depth = 3			Depth = 4
Total # of nodes generated per round 	66.0				231.4375			3467.4166666666665
Total # of duplicate nodes per round 	54.29032258064516.		188.125				2859.3333333333335
Average branching factors 		6.162650602409639.		5.366666666666666		5.474868421052632
Runtime per round 			0.09794908954251197.		0.2257421538233757		2.982421894868215
Score (student vs. greedy)		53 vs. 11			59 vs. 5			N/A
Remaining time (student vs. greedy)	26.99999999999998 vs. 30.0	22.799999999999983 vs. 30.0	N/A
Results					student wins			student wins			student ran out of time
run 10 times, student wins #		10/10				10/10				student ran out of time

Since it's always run out of time when depth = 4, we only run on depth = 2 and depth = 3 for the following experiment. 

Table 3: Minimax Search vs. Random1 Results (python3 othello.py student random1)
					Depth = 2			Depth = 3			
Total # of nodes generated per round 	74.93548387096774		687.3636363636364			
Total # of duplicate nodes per round 	62.70967741935484		624.4242424242424			
Average branching factors 		6.675287356321839		10.957971014492754		
Runtime per round 			0.06182026094005954		0.5538872588764537				
run 10 times, student wins #		10/10				7/10				

Table 4: Alpha-beta Pruning Minimax Search vs. Random1 Results (python3 othello.py student random1 -aB)
					Depth = 2			Depth = 3			
Total # of nodes generated per round 	59.354838709677416		632.5333333333333			
Total # of duplicate nodes per round 	48.58064516129032		551.9666666666667				
Average branching factors 		6.072607260726072		7.854304635761589		
Runtime per round 			0.04626491761976673		0.550691294670105		
run 10 times, student wins #		10/10				10/10	

Table 5: Minimax Search vs. Random2 Results (python3 othello.py student random2)
					Depth = 2			Depth = 3			
Total # of nodes generated per round 	81.78125			1454.1304347826087			
Total # of duplicate nodes per round 	68.5625				1347.9565217391305				
Average branching factors 		6.69309462915601		13.701351904956985		
Runtime per round 			0.06425772607326508		1.3388568111087964		
run 10 times, student wins #		10/10				6/10

Table 6: Alpha-beta Pruning Minimax Search vs. Random2 Results (python3 othello.py student random2 -aB)
					Depth = 2			Depth = 3			
Total # of nodes generated per round 	81.54838709677419		559.516129032258			
Total # of duplicate nodes per round 	69.58064516129032		481.3225806451613				
Average branching factors 		7.435294117647059		7.164394878149525		
Runtime per round 			0.06925120661335607		0.4750114025608186		
run 10 times, student wins #		10/10				10/10	

Table 7: Minimax Search vs. Random3 Results (python3 othello.py student random3)
					Depth = 2			Depth = 3			
Total # of nodes generated per round 	73.66666666666667		942.8666666666667			
Total # of duplicate nodes per round 	62.56666666666667		858.9333333333333				
Average branching factors 		7.293729372937293		11.237981724274931		
Runtime per round 			0.05777432918548584		0.7783665736516316		
run 10 times, student wins #		10/10				7/10

Table 8: Alpha-beta Pruning Minimax Search vs. Random3 Results (python3 othello.py student random3 -aB)
					Depth = 2			Depth = 3			
Total # of nodes generated per round 	62.8				529.9666666666667			
Total # of duplicate nodes per round 	52.3				451.06666666666666				
Average branching factors 		6.610526315789474		6.722621564482029		
Runtime per round 			0.047529228528340656		0.43690512975056967		
run 10 times, student wins #		10/10				10/10	

Reference:
[1] Li and Radichkov, Mini-Othello, https://www.cs.cornell.edu/~yuli/othello/othello.html


