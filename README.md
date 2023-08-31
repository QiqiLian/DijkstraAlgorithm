# DijkstraAlgorithm
Usage
Run the program by executing the main.py file in a Python interpreter.
The program will prompt you to enter the number of edges in the graph.
For each edge, provide the source vertex, destination vertex, and the edge weight.
Enter the starting vertex from which you want to find the shortest distances.
The program will output the shortest distances from the starting vertex to all other vertices in the graph.
Code Explanation
The program is organized into two classes:

Graph Class: This class represents the graph and provides methods to add edges and find the shortest distances using Dijkstra's algorithm. The graph is represented using an adjacency list.

main Function: The main function takes user input to create a graph, add edges, and find the shortest distances. It interacts with the Graph class to perform these operations.

The program uses a priority queue implemented as a heap to efficiently perform Dijkstra's algorithm.

Input Format
The program expects the following inputs:

Number of edges in the graph.
For each edge:
Source vertex.
Destination vertex.
Edge weight.
Starting vertex to find the shortest distances from.
