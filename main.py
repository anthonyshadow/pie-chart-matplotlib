import matplotlib.pyplot as plt

labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'
sizes = [33, 52 , 12, 17, 62, 48]

#set numbers for items we want seperated and 0 for those we want attached
seperated = (.1, 0, 0, 0, 0 ,0)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=seperated)
plt.axis('equal')

plt.show()