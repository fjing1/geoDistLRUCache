#### This is a take home TECHNICAL TEST I had during interview. I found this is extremely useful and good topic. After I completed and received the 2nd round interview on Nov 1st, I decide to add more function into it. So it become a personal project starting on 2023 Nov 1st. 

  

Question A 

Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8). 

  

Question B 

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of. 

  

Question C 

We want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria: 

  

    1 - Simplicity. Integration needs to be dead simple. 

    2 - Resilient to network failures or crashes. 

    3 - Near real time replication of data across Geolocation. Writes need to be in real time. 

    4 - Data consistency across regions 

    5 - Locality of reference, data should almost always be available from the closest region 

    6 - Flexible Schema 

    7 - Cache can expire  

As a hint, we are not looking for quantity, but rather quality, maintainability, scalability, testability and a code that you can be proud of.  

When submitting your code add the necessary documentation to explain your overall design and missing functionalities.  Do it to the best of your knowledge. 


On Nov 1st, I added the check consistency for the replication part in replication.py and main.py, the idea I had is for multiple secondary database or cache available, pick the highest consistent ones. 
In the future, I am thinking adding a manager to coordinate the secondary picks.

Nov 4th, distributed operating system would be a use case for such caching. Adding an issue for this. 
