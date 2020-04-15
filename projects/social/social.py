import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # use add_user method num_users times

        # Create friendships
        for i in range(0, num_users):
            self.add_user(f"User {i }")
        # Generate all friendship combinations
        possible_friendships = []
        # Avoid duplicates by making sure first number is smaller  than second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))
        # shuffle all possible friendships
        random.shuffle(possible_friendships)
        # create for first X pairs, x is total // 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        # * Hint 1: To create N random friendships, you could create a list with all possible friendship combinations, shuffle the list, then grab the first N elements from the list. You will need to import random to get shuffle.

        # * Hint 2: add_friendship(1, 2) is the same as add_friendship(2, 1). You should avoid calling one after the other since it will do nothing but print a warning. You can avoid this by only creating friendships where user1 < user2.

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # !!!! IMPLEMENT ME
        # We want to find the the shortest path from user_id to each of its extended network of friends
        # shortest path is a clue that we want to use a BFT
        # We can probably use the BFT method we made earlier with some modifications
        
        #initialize a queue
        que = Queue()
        #enqueue a path to the first user
        que.enqueue([user_id])
        visited = {}  # Note that this is a dictionary, not a set
        #while the queue is not empty
        while que.size() > 0:
            #dequeue the first path
            path = que.dequeue()
            # grab the last id from the path and make it the current id
            current_id = path[-1]
            # print(f'current_id:{current_id}')
            # check if the current id is in visited
            if current_id not in visited:
                # if not, add the current id as the key and the path as the value
                visited[current_id] = path
                # print(f'path{path}')
                #iterate through the friends of the current id
                for friend in self.friendships[current_id]:
                    # create a copy of the path
                    new_path = list(path)
                    # append each friend
                    new_path.append(friend)
                    # enqueue the new path
                    que.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f'friendships {sg.friendships}')
    connections = sg.get_all_social_paths(1)
    print(f'connections: {connections}')
