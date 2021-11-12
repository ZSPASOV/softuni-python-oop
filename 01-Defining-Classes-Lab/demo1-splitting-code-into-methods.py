# We use methods to split code into functional blocks
# Improves code readability
# Allows for easier debugging

# v1
# for move in moves:
#   for row in range(len(room)):
#     for col in range(len(room[row])):
#       if room[row][col] == 'b':
#         …

# v2
# for move in moves:
#     move_enemies()
#     killer_check()
#     move_player(move)

# A single method should complete a single task


# do_magic ( … )
# deposit_or_withdraw ( … )
# deposit_and_get_balance ( … )
# parse_data_and_return_result ( … )

# INSTEAD OF THE APPROACH ABOVE YOU SHOULD USE THE APPROACH BELOW:

# withdraw ( … )
# deposit ( … )
# getBalance ( … )
# toString ( … )
