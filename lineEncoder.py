import matplotlib.pyplot as plt
import numpy as np

class Stream:
  def __init__(self,_stream):
    self.stream = _stream
    self.time = np.arange(len(self.stream)*2) + 1
    self.encoded = np.zeros(len(self.stream)*2)

  def manchester_encode(self):
          for T in range(len(self.stream)): #for every T period of bit rate
                  i = 2*T   #first half period T
                  k = 2*T +1 #second half period T
                  #print(T,i,k)
                  
                  if(self.stream[T] == 1):  # if 1
                          self.encoded[i] = 1
                          self.encoded[k] = 0
                  elif(self.stream[T] != 1): # if 0
                          self.encoded[i] = 0
                          self.encoded[k] = 1
                  print(self.encoded[i], self.encoded[k])
  def unipolar_nrz_encode(self):
          for T in range(len(self.stream)):
                  i = 2*T   #first half period T
                  k = 2*T +1 #second half period T
                  #print(T,i,k)
                  
                  if(self.stream[T] == 1):  # if 1
                          self.encoded[i] = 1
                          self.encoded[k] = 1
                  elif(self.stream[T] != 1): # if 0
                          self.encoded[i] = 0
                          self.encoded[k] = 0
                  print(self.encoded[i], self.encoded[k])
  def polar_nrz_encode(self):
          for T in range(len(self.stream)):
                  i = 2*T   #first half period T
                  k = 2*T +1 #second half period T
                  #print(T,i,k)
                  
                  if(self.stream[T] == 1):  # if 1
                          self.encoded[i] = 1
                          self.encoded[k] = 1
                  elif(self.stream[T] != 1): # if 0
                          self.encoded[i] = -1
                          self.encoded[k] = -1
                  print(self.encoded[i], self.encoded[k])
  def unipolar_rz_encode(self):
          for T in range(len(self.stream)):
                  i = 2*T   #first half period T
                  k = 2*T +1 #second half period T
                  #print(T,i,k)
                  
                  if(self.stream[T] == 1):  # if 1
                          self.encoded[i] = 1
                          self.encoded[k] = 0
                  elif(self.stream[T] != 1): # if 0
                          self.encoded[i] = 0
                          self.encoded[k] = 0
                  print(self.encoded[i], self.encoded[k])
  def bipolar_rz_encode(self):
          flag = True
          for T in range(len(self.stream)):
                  i = 2*T   #first half period T
                  k = 2*T +1 #second half period T
                  #print(T,i,k)
                  
                  if(self.stream[T] == 1):  # if 1
                          if(flag == True):
                                  self.encoded[i] = 1
                                  self.encoded[k] = 0
                                  flag = False
                          elif(flag == False):
                                  self.encoded[i] = -1
                                  self.encoded[k] = 0
                  elif(self.stream[T] != 1): # if 0
                          self.encoded[i] = 0
                          self.encoded[k] = 0
                  print(self.encoded[i], self.encoded[k])




traza = Stream([1,1,0,1,0,0,1])
traza.bipolar_rz_encode()
fig, ax = plt.subplots()
x = traza.time
y = traza.encoded
ax.step(x, y, linewidth=2.5)

ax.set(xlim=(0, len(traza.stream)*2), xticks=np.arange(0, len(traza.stream)*2),
	       ylim=(-2, 2), yticks=np.arange(0, 2))

plt.show()