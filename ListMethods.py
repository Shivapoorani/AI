print("List Methods")
animals = ['cat', 'dog', 'rabbit']
animals1 = ['tiger', 'fox']
animals1.append("wolf")
print("Added List: ",animals1)
animals.append(animals1)
print("Append list: ", animals)
animals.extend(animals1)
print("Extended List: ",animals)
animals.remove("rabbit")
print("Deleted List: ",animals)
