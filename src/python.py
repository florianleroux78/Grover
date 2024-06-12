
import matplotlib.pyplot as plt


import qsharp

qsharp.init(project_root = '../Grover')


nbQubits = [3, 5, 10]
trys = 500
print(nbQubits)


resultatsDesSimulations = []

for nb in nbQubits:
    liste_try = []
    for tryeeh in range(trys):
        call = "Grover.Main(" + str(nb) + ")"
        res = qsharp.eval(call)

        lenRes = len(res)
        i = lenRes
        state = 0

        for element in res :
            
            if element == qsharp.Result.One:
                state += (2 ** i)
            i -= 1
            
        liste_try.append(state)
    
    resultatsDesSimulations.append(liste_try)
    

print(resultatsDesSimulations)


# Les résultats que tu as fournis
results_N3 = resultatsDesSimulations[0]
results_N5 =  resultatsDesSimulations[1]
results_N10 =  resultatsDesSimulations[2]

# Fonction pour calculer les probabilités à partir des comptes bruts
def calculate_probabilities(counts):
    total_counts = sum(counts)
    probabilities = [count / total_counts for count in counts]
    return probabilities

# Calcul des probabilités pour chaque valeur de N
probabilities_N3 = calculate_probabilities(results_N3)
probabilities_N5 = calculate_probabilities(results_N5)
probabilities_N10 = calculate_probabilities(results_N10)

# Tracer les courbes
iterations_range = range(1, len(results_N3) + 1)

plt.figure(figsize=(12, 8))
plt.plot(iterations_range, probabilities_N3, label='N = 2^3', marker='o')
plt.plot(iterations_range, probabilities_N5, label='N = 2^5', marker='o')
plt.plot(iterations_range, probabilities_N10, label='N = 2^10', marker='o')

plt.xlabel('Nombre d\'itérations')
plt.ylabel('Probabilité de mesurer l\'état marqué')
plt.title('Probabilité de mesurer l\'état marqué vs Nombre d\'itérations pour différentes valeurs de N')
plt.legend()
plt.grid(True)
plt.show()