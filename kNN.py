### k-Nearest Neighbors ###

# Using kNN to classify data #
# Following along with class notes #

### Video 1
import numpy as np

def distance(p1, p2):
'''Finds distance between 2 points'''
  return np.sqrt(np.sum(np.power(p2-p1, 2)))

p1 = np.array([1,1])
p2 = np.array([4,4])
distance(p1,p2)
# Returns: 4.242640687118...

### Video 2
import random
import scipy.stats as ss

def majority_vote(votes):
  '''Returns most common element'''
  vote_counts = {}
  for vote in votes:
    if vote in vote_counts:
      vote_counts[vote] += 1
    else:
      vote_counts[vote] = 1
  winners = []
  max_count = max(vote_counts.values())
  for vote, count in vote_counts.items():
    if count == max_count:
      winners.append(vote)
  return random.choise(winners)
  
def majority_vote_short(votes):
  '''returns most common element'''
  mode, count = ss.mstats.mode(votes)
  return mode
  
votes = [1,2,3,1,2,3,3,3,3,2,2,2]
majority_vote(votes)
# returns 2 or 3 randomly
majority_vote_short(votes)
# returns 2

### Video 3
## creating a simple kNN algorithm

import numpy as np
points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])
p = np.array([2.5, 2])

import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], "ro")
plt.plot(p[0], p[1], "bo)
plt.axis([0.5, 3.5, 0.5, 3.5])

distances = np.zeros(points.shape[0])
for loop in range(len(distances)):
  distances[loop] = distance(p, points[loop])

