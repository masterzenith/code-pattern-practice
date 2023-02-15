"""
Degrees Of Separation
From Wikipedia, the concept of six degrees of separation "is the idea that all people are six, or fewer, social
connections away from each other."
For example, if Clement and Antoine are friends, they share one degree of separation. If Simon is Antoine's friend but
not Clement's friend, then Clement and Simon share two degrees of separation, since they're connected by Antoine.
You're given a directory of friends lists (a map of people's names pointing to lists of their friends' names) as well
as the names of two people (found in the directory).
Write a function that returns the name of the person (one of the two input names) that is more than six degrees of
separation away from the fewest amount of people (in the directory).
If both input persons have the same number of people who are more than six degrees of separation away, your function
should return the empty string "".
Note that if Antoine is Clement's friend, it follows that Clement is Antoine's friend. Thus, if person A's name is found
in person B's friends list, then person B's name will be found in person A's friends list.
Sample Input:
friendsList = {
  "Aaron": ["Paul"],
  "Akshay": [],
  "Alex": ["Antoine", "Clement", "Ryan", "Simon"],
  "Antoine": ["Alex", "Clement", "Simon"],
  "Ayushi": ["Lee"],
  "Changpeng": ["Kelly", "Sandeep"],
  "Clement": ["Alex", "Antoine", "Sandeep", "Simon"],
  "Hannah": ["Lexi", "Paul", "Sandeep"],
  "James": ["Paul"],
  "Kelly": ["Changpeng", "Molly"],
  "Lee": ["Ayushi", "Molly"],
  "Lexi": ["Hannah"],
  "Molly": ["Kelly", "Lee"],
  "Paul": ["Aaron", "James", "Hannah"],
  "Ryan": ["Alex"],
  "Sandeep": ["Changpeng", "Clement", "Hannah"],
  "Simon": ["Alex", "Antoine", "Clement"]
},
personOne = "Antoine"
personTwo = "Clement"

Sample Output:
"Clement"
// Neither Antoine nor Clement have any connection to Akshay.
// Antoine is seven degrees of separation away from Ayushi.
// So Clement only has one person who is more than six degrees of
// separation away (Akshay), whereas Antoine has two (Akshay and Ayushi).
"""


def six_degrees_of_separation(directory, person1, person2):
    # initialize counts for person1 and person2
    person1_count = 0
    person2_count = 0

    # initialize sets for tracking visited people
    person1_visited = set()
    person2_visited = set()

    # initialize queues for BFS traversal
    person1_queue = [(person1, 0)]
    person2_queue = [(person2, 0)]

    while person1_queue or person2_queue:
        # traverse person1's friends
        if person1_queue:
            curr_person, curr_degrees = person1_queue.pop(0)
            if curr_person in directory:
                for friend in directory[curr_person]:
                    if friend not in person1_visited:
                        person1_visited.add(friend)
                        if curr_degrees + 1 <= 6:
                            person1_queue.append((friend, curr_degrees + 1))
                        else:
                            person1_count += 1

        # traverse person2's friends
        if person2_queue:
            curr_person, curr_degrees = person2_queue.pop(0)
            if curr_person in directory:
                for friend in directory[curr_person]:
                    if friend not in person2_visited:
                        person2_visited.add(friend)
                        if curr_degrees + 1 <= 6:
                            person2_queue.append((friend, curr_degrees + 1))
                        else:
                            person2_count += 1

    # compare counts and return result
    if person1_count < person2_count:
        return person1
    elif person1_count > person2_count:
        return person2
    else:
        return ""


def main():
    friendsList = {
                      "Aaron": ["Paul"],
                      "Akshay": [],
                      "Alex": ["Antoine", "Clement", "Ryan", "Simon"],
                      "Antoine": ["Alex", "Clement", "Simon"],
                      "Ayushi": ["Lee"],
                      "Changpeng": ["Kelly", "Sandeep"],
                      "Clement": ["Alex", "Antoine", "Sandeep", "Simon"],
                      "Hannah": ["Lexi", "Paul", "Sandeep"],
                      "James": ["Paul"],
                      "Kelly": ["Changpeng", "Molly"],
                      "Lee": ["Ayushi", "Molly"],
                      "Lexi": ["Hannah"],
                      "Molly": ["Kelly", "Lee"],
                      "Paul": ["Aaron", "James", "Hannah"],
                      "Ryan": ["Alex"],
                      "Sandeep": ["Changpeng", "Clement", "Hannah"],
                      "Simon": ["Alex", "Antoine", "Clement"]
                  }
    personOne = "Antoine"
    personTwo = "Clement"
    print(six_degrees_of_separation(friendsList, personOne, personTwo))


if __name__ == "__main__":
    main()
