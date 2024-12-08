import matplotlib.pyplot as plt

def plot_ats_score(score):
    labels = ['Matched', 'Unmatched']
    sizes = [score, 100-score]
    colors = ['#4CAF50', '#FF5733']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%', startangle=90)
    plt.title(f"ATS Score :{score}%")
    plt.axis('equal')
    plt.show()