'''A group of statisticians at a local college has asked you to create a set of functions 
that compute the median and mode of a set of numbers, as defined in Section 
5.4. Define these functions in a module named stats.py. Also include a function 
named mean, which computes the average of a set of numbers. Each function 
should expect a list of numbers as an argument and return a single number. Each 
function should return 0 if the list is empty. Include a main function that tests the 
three statistical functions with a given list.'''
def main():
    set_of_numbers = []
    print("the mode is:",find_mean(set_of_numbers))
    print('the median is:', find_median(set_of_numbers))
    print('the mode is:', find_mode(set_of_numbers))

def find_mean(set_of_numbers):
    if not set_of_numbers:
        return 0
    sum_of_numbers = sum(set_of_numbers)
    length_of_numbers = len(set_of_numbers)
    total_mean = sum_of_numbers / length_of_numbers
    return total_mean


def find_median(set_of_numbers):
    if not set_of_numbers:
        return 0
    
    set_of_numbers.sort()
    midpoint = len(set_of_numbers) // 2
    if len(set_of_numbers) % 2 == 1:
      result =  (set_of_numbers[midpoint])
    else:
      result =  ((set_of_numbers[midpoint] + set_of_numbers[midpoint - 1]) / 2)
    return result

def find_mode(set_of_numbers):
    if not set_of_numbers:
        return 0
    theDic ={}
    for word in set_of_numbers:
        number =  theDic.get(word,None)
        if number == None:
            theDic[word] = 1
        else:
            theDic[word] = number + 1
    theMaximun = max(theDic.values())
    for key in theDic:
        if theDic[key] == theMaximun:
            return key    

    
if __name__ == '__main__':
    main()