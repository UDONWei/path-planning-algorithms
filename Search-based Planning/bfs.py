#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: huiming zhou
"""

import queue
import tools
import env
import motion_model


class BFS:
    def __init__(self, x_start, x_goal):
        self.u_set = motion_model.motions                             # feasible input set
        self.xI, self.xG = x_start, x_goal
        self.obs = env.obs_map()                                      # position of obstacles

        tools.show_map(self.xI, self.xG, self.obs, "breadth-first searching")


    def searching(self):
        """
        Searching using BFS.

        :return: planning path, action in each node, visited nodes in the planning process
        """

        q_bfs = queue.QueueFIFO()                                     # first-in-first-out queue
        q_bfs.put(self.xI)
        parent = {self.xI: self.xI}                                   # record parents of nodes
        action = {self.xI: (0, 0)}                                    # record actions of nodes

        while not q_bfs.empty():
            x_current = q_bfs.get()
            if x_current == self.xG:
                break
            if x_current != self.xI:
                tools.plot_dots(x_current, len(parent))
            for u_next in self.u_set:                                 # explore neighborhoods of current node
                x_next = tuple([x_current[i] + u_next[i] for i in range(len(x_current))])
                if x_next not in parent and x_next not in self.obs:   # node not visited and not in obstacles
                    q_bfs.put(x_next)
                    parent[x_next] = x_current
                    action[x_next] = u_next
        [path_bfs, action_bfs] = tools.extract_path(self.xI, self.xG, parent, action)     # extract path

        return path_bfs, action_bfs


if __name__ == '__main__':
    x_Start = (5, 5)                    # Starting node
    x_Goal = (49, 5)                    # Goal node
    bfs = BFS(x_Start, x_Goal)
    [path_bf, actions_bf] = bfs.searching()
    tools.showPath(x_Start, x_Goal, path_bf)
