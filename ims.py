from datetime import datetime
start_time = datetime.now()
from PIL import Image
# sorting algorithm
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
     
    L = [0] * (n1) 
    R = [0] * (n2) 
    
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
   
    i = 0      
    j = 0     
    k = l      
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
   
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
 
def mergeSort(arr,l,r): 
    if l < r: 
        
        m = (l+(r-1))//2
        
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r)
# searching algorithm
def search(x):
 if x in h.keys():
     print("image is found")
     f1['image'].show()
 else:
     print("\nimage is not found\n")
     print("the given image does not match with the images present \n")
     print("the given image is %d" %x)
# main function             
f =[]
g =[]
t="Enter the number of images you want to insert : ";
n=int(input(t));
for i in range(n):
    j=i+1;
    a=input("Give the location of image %d :" % j)
    image = Image.open(a)    
    [width, length] = image.size
    s1 = width*length
    g.append(s1)
    f.append([s1,image]);
    print(image)
    image.show()
# print images in list
print ("Given images list is")  
print(f)
# sorting images using merge sort
mergeSort(f,0,n-1) 
# print sorted images and display
print ("\n\nSorted array is") 
print(f)
h = dict(f)
for key in h:
    k = h[key]
    k.show()
# searching for input image in given image list
print("All the images have been sorted based on thier size")
t1="Enter the path of the image you want to search :";
k=input(t1);
image2 = Image.open(k)
print(image2)
[width2,length2]=image2.size
s2 = width2*length2
f1 = {'size':s2,'image':image2}
a2 = f1['size']
search(a2)
end_time = datetime.now()
print('Duration:{}' .format(end_time - start_time))