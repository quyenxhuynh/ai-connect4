def minimax(game_state):
    return None

# from pacman

# def max_value(agent, gameState, depth):
#     if gameState.isWin() or gameState.isLose() or depth == agent.depth:  # checks if state is terminal
#         return [agent.evaluationFunction(gameState), None]
#     cur_max = -99999999
#     action = None
#     successors = gameState.getLegalActions(0)  # Pacman is always index 0
#     for successor in successors:
#         new_max = min_value(agent, gameState.generateSuccessor(0, successor), depth, 1)[0]
#         if new_max >= cur_max:
#             cur_max = new_max
#             action = successor
#     return [cur_max, action]
#
#
# def min_value(agent, gameState, depth, index):
#     if gameState.isWin() or gameState.isLose() or depth == agent.depth:  # checks if state is terminal
#         return [agent.evaluationFunction(gameState), None]
#     #  want to call min_value for each ghost except last
#     if index < gameState.getNumAgents() - 1:
#         cur_min = 99999999
#         action = None
#         successors = gameState.getLegalActions(index)
#         for successor in successors:
#             new_min = min_value(agent, gameState.generateSuccessor(index, successor), depth, index + 1)[0]
#             if new_min <= cur_min:
#                 cur_min = new_min
#                 action = successor
#         return [cur_min, action]
#     else:  # last ghost
#         cur_min = 99999999
#         action = None
#         successors = gameState.getLegalActions(index)
#         for successor in successors:
#             new_min = max_value(agent, gameState.generateSuccessor(index, successor), depth + 1)[0]
#             if new_min <= cur_min:
#                 cur_min = new_min
#                 action = successor
#         return [cur_min, action]
