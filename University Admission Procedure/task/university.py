class Admission:
    def __init__(self):
        self.scores = []
        self.mean_score = None
        self.m_places = None
        self.places_left = []
        self.winners = [[], [], [], [], []]
        self.score_index = {"Biotech": (2, 3), "Physics": (2, 4), "Chemistry": 3, "Mathematics": 4, "Engineering": (4, 5)}
        self.applicants = []
        self.round = None
        self.majors = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
        self.get_config()
        self.get_applicants()
        self.admit()
        self.sort_winners()
        self.show_results()
        self.write_results()

    def get_config(self):
        self.m_places = int(input())
        self.places_left = [self.m_places] * 5

    def get_applicants(self):
        with open('applicants.txt') as applicants:
            self.applicants.extend([applicant.split() for applicant in applicants])

    def admit(self):
        for self.round in range(3):
            for i, major in enumerate(self.majors):
                [self.winners[i].append(winner) for winner in self.admit_major(major=major)]

    def admit_major(self, major):
        applicants = filter(lambda x: x[self.round + 7] == major, self.applicants)
        winners = sorted(sorted(applicants, key=lambda x: (x[0], x[1])), reverse=True, key=lambda x: max(float(x[6]), float(x[self.score_index[major]]) if type(self.score_index[major]) == int else (int(x[self.score_index[major][0]]) + int(x[self.score_index[major][1]])) / 2))[:self.places_left[self.majors.index(major)]]
        self.places_left[self.majors.index(major)] -= len(winners)
        [self.applicants.remove(winner) for winner in winners]
        return winners

    def sort_winners(self):
        for i, major in enumerate(self.winners):
            self.winners[i] = sorted(sorted(major, key=lambda x: (x[0], x[1])), reverse=True, key=lambda x: max(float(x[6]), float(x[self.score_index[self.majors[i]]]) if type(self.score_index[self.majors[i]]) == int else (int(x[self.score_index[self.majors[i]][0]]) + int(x[self.score_index[self.majors[i]][1]])) / 2))

    def show_results(self):
        for i, major in enumerate(self.majors):
            print(major)
            print(*[f"{applicant[0]} {applicant[1]} {max(float(applicant[6]), float(applicant[self.score_index[major]]) if type(self.score_index[major]) == int else round((int(applicant[self.score_index[major][0]]) + int(applicant[self.score_index[major][1]])) / 2, ndigits=1))}" for applicant in self.winners[i][:self.m_places]], sep='\n', end='\n\n')

    def write_results(self):
        for i, major in enumerate(self.majors):
            with open(major.lower() + ".txt", "w") as file:
                print(*[f"{applicant[0]} {applicant[1]} {max(float(applicant[6]), float(applicant[self.score_index[major]]) if type(self.score_index[major]) == int else (int(applicant[self.score_index[major][0]]) + int(applicant[self.score_index[major][1]])) / 2)}" for applicant in self.winners[i][:self.m_places]], sep='\n', end='\n\n', file=file)


admission = Admission()
