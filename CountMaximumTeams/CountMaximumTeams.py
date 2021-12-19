#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
###################################################################################
Author:  Vamsi Yalamanchili
Date:    18-Dec-2021

Problem: Each team can have teamSize of developers
         A developer's skill level is denoted by skill[i]   
         The difference between the maximum and minimum skill levels with in a team cannot exceed a threshold, maxDiff.
         Return the maximum number of teams that can formed from the contestants when skill, teamSize and maxDiff is given
Example1: 
 skill: [3,4,3,1,6,5]
 teamSize: 3
 maxDiff: 2

 Output: 2 - Atmost 2 teams can be formed. [3,3,1], [4,6,5]

Example2: 
 skill: [5,1,2,1,4,5]
 teamSize: 3
 maxDiff: 2

 Output: 2 - Atmost 2 teams can be formed. [2,1,1], [4,5,5]

 Example3: 
 skill: [9,3,5,7,1]
 teamSize: 2
 maxDiff: 1

 Output: 0 - no teams can be formed
###################################################################################
 Time Complexity:

 Worst Case   - O(n)      - When no teams can be formed, loop through all the members in the skill dataset
 Average Case - O(log(n)) - Incase of team formed, we are skipping team size for every team formed.
###################################################################################
"""
def countMaximumTeams(skill, teamSize, maxDiff):

    #Sort the skill list to ensure minumum comparisions and not to repeat same checks
    skill.sort()

    #i is index for the team member with minimum skill
    #cnt is to track the number of teams that can be formed
    i = cnt = 0
    j = teamSize - 1  #j helps to extract one team(with teamSize) in 1 iteratiom
    len1 = len(skill)
    
    while(j < len1):

        #compare minimum skilled team member (i) with maximum skilled team member (j)
        if(skill[j] - skill[i] <= maxDiff):
            cnt += 1                                #Increase the team formation count
            i = j + 1                               #Increase i to 1 beyond j to start searching for new team
            j = i + teamSize - 1                    #Increase j to new team maximum skilled member
        else:                                       #case when team cannot be formed with i, j combination
            i += 1                                  #Increment i to the next team member
            j += 1                                  #Increment j to the next team member
    return cnt

if __name__ == "__main__":

    skill =  [3,4,3,1,6,5]
    teamSize = 3
    maxDiff = 2
    print("#####################################################################################")
    print("Input Skill:", skill)
    print("Input Team Size:", teamSize)
    print("Input Max Diff:", maxDiff)
    
    print("Output:", countMaximumTeams(skill, teamSize, maxDiff),"teams can be formed")
    print("#####################################################################################")
    skill =  [5,1,2,1,4,5]
    teamSize = 3
    maxDiff = 2

    print("Input Skill:", skill)
    print("Input Team Size:", teamSize)
    print("Input Max Diff:", maxDiff)
    
    print("Output:", countMaximumTeams(skill, teamSize, maxDiff),"teams can be formed")
    print("#####################################################################################")

    skill =  [9,3,5,7,1]
    teamSize = 2
    maxDiff = 1

    print("Input Skill:", skill)
    print("Input Team Size:", teamSize)
    print("Input Max Diff:", maxDiff)
    
    print("Output:", countMaximumTeams(skill, teamSize, maxDiff),"teams can be formed")    
    print("#####################################################################################")
