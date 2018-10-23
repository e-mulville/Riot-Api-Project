# Riot-Api-Project

This is my side project to familiarise myself with Python after mostly programming in C++.

To practice navigating the game list and manipulating data I have made a function to work out the average performance of a summoners teammates vs their oppenents.

The current goal is to gather and store match data in a numpy array. This is necassary as I can only make 1 API request per second so gathering all the data necassary for analysis on each run of the program would take too long. Instead I aim to have a function to gather a large amount of match data and store it in a file for use later.

After that the goal is to see if I can train a neural networks to predict who will win at the beginning of the game. 

The final goal is to work out key features in wins and losses using neural networks.

This will mostly exploit the Riot Games API to gain access to data from League of Legends.
