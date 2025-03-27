# Distributed-Data-Servers
Distributed Data Servers
A server network is represented as a tree of g_nodes servers indexed from 1 to g nodes and g_nodes - 1 edges where the ith edges connect the servers g from[i] and g_toli]. The transfer time between any two connected servers is 1 unit.
Given the graph g, find the maximum time taken to transfer the data between any two servers in the system.
Example:
Suppose g_nodes = 3, g_ from = [1, 2], g_to = [2, 3].
The maximum time is required to transfer data from 1 to 3 that takes 2 units of time. Hence, the answer is 2.

Function Description
Complete the function getMaxTime in the editor below.
getMaxTime has the following parameters:
int &nodes. the number of servers in the network int g_ from[n]: the end point of the edges int g_to[n]: the end point of the edges
Returns
servers
int: the maximum time to transfer the data between any two
Constraints
*   15 gnodes ≤ 5*104
*   1 ≤ gfrom. g_to≤ & nodes
*   Input Format For Custom Testing
*   Sample Case 0
