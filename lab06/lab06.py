from Apartment import Apartment
def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]
        
        mergesort(lefthalf)
        mergesort(righthalf)
        i = 0 
        j = 0 
        k = 0 

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i = i + 1
            else:
                apartmentList[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i = i + 1
            k = k + 1
            
        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j = j + 1
            k = k + 1

def ensureSortedAscending(apartmentList):
    if len(apartmentList) == 0:
        return True
    num = 0
    while (num+1) <= len(apartmentList) - 1:
        if apartmentList[num] < apartmentList[num+1]:
            num += 1
        else:
            return False
    else:
        return True

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    best = apartmentList[0]
    return best.getApartmentDetails()

def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    worst = apartmentList[-1]
    return worst.getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    mergesort(apartmentList)
    budget_list = ''
    for i in range(len(apartmentList)):
        if apartmentList[i].getRent() <= budget:
            budget_list += apartmentList[i].getApartmentDetails() + '\n'
    return budget_list.rstrip()