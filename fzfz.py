def secondary_rounds_method(self, round_played, tournament_played):
    """Generates a round 2,3,4 matches list without redundancy with the previous match_ups
    Args : round instance, tournament instance"""
    player_list = self.player_list_score_generator(tournament_played)
    round_ranking = self.player_list_sorting_score(player_list, False)
    match_list = []
    match_count = 0
    players_list = []
    for i in round_ranking:
        players_list.append(i.id)
    pairs = self.possible_pairs(round_played.tournament_name, players_list)
    match_up_list = self.list_comb_recursive(pairs)
    for j in match_up_list:
        match_count += 1
        match_name = "Match " + str(match_count)
        player_one_creation = self.database.search_in_data_base("Player", j[0])
        player_one_instance = self.player_instance_creation_from_data_base(player_one_creation)
        self.player_score_generator_round(player_one_instance, tournament_played, round_played.id)
        player_two_creation = self.database.search_in_data_base("Player", j[1])
        player_two_instance = self.player_instance_creation_from_data_base(player_two_creation)
        self.player_score_generator_round(player_two_instance, tournament_played, round_played.id)
        match_i = Match(match_name, player_one_instance, player_two_instance, round_played, 0)
        print(match_i)
        self.database.database_item_insertion("Match", match_i.serialized_form)
        match_list.append(match_i)
    round_played.matches_list = match_list
    return match_list


def possible_pairs(self, tournament_id, players_list):
    """ Defines all the possible match_up pairs (including already played
    Args: tournament id, player_list_instances"""
    players = players_list
    pairs = self.database.list_match_pairs(tournament_id)
    possible_match_ups = []
    for i in range(8):
        for j in range(i + 1, 8):
            if [players[i], players[j]] not in pairs:
                possible_match_ups.append([players[i], players[j], i + j])
    possible_match_ups.sort(key=lambda x: x[2], reverse=True)
    return possible_match_ups


@staticmethod
def check_player_exist(list_matches, match):
    """Check if a match_up pair has already be played"""
    for i in list_matches:
        if match[0] == i[0] or match[0] == i[1] or match[1] == i[0] or match[1] == i[1]:
            return False
    return True


def try_recursive(self, list_comb, list2, i, count_number):
    """Recursive match creation (up until 4)
    Try to append all matches and check if they have already been played"""
    for i in range(i, len(list_comb)):
        if len(list2) > count_number:
            list2.pop()
        if self.check_player_exist(list2, list_comb[i]):
            list2.append(list_comb[i])
            count_number += 1
            j = i + 1
            return self.try_recursive(list_comb, list2, j, count_number)


def list_comb_recursive(self, list_comb):
    """Launch function for the recursive
    Arg : possible match-ups list"""
    list2 = []
    count_number = 0
    i = 0
    self.try_recursive(list_comb, list2, i, count_number)
    return list2