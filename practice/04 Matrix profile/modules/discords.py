import numpy as np

from modules.utils import *

# def top_k_discords(matrix_profile: dict, top_k: int = 3) -> dict:
#     """
#     Find the top-k discords based on matrix profile

#     Parameters
#     ---------
#     matrix_profile: the matrix profile structure
#     top_k: number of discords

#     Returns
#     --------
#     discords: top-k discords (indices, distances to its nearest neighbor and the nearest neighbors indices)
#     """
 
#     discords_idx = []
#     discords_dist = []
#     discords_nn_idx = []

#     # INSERT YOUR CODE
#     mp = matrix_profile['mp']
#     mpi = matrix_profile['mpi']
#     exclusion_zone = matrix_profile.get('excl_zone', 0)
#     m = matrix_profile['m']

#     mp_copy = mp.copy()

#     for _ in range(top_k):
#         # Find the largest distance in the matrix profile
#         max_dist_idx = np.argmax(mp)
#         max_dist = mp[max_dist_idx]

#         # Get the index of the nearest neighbor
#         nn_idx = mpi[max_dist_idx]

#         # Append discord information
#         discords_idx.append(max_dist_idx)
#         discords_dist.append(max_dist)
#         discords_nn_idx.append(nn_idx)

#         # Apply exclusion zone to avoid trivial matches
#         apply_exclusion_zone(mp_copy, max_dist_idx, exclusion_zone, -np.inf)
#         apply_exclusion_zone(mp_copy, nn_idx, exclusion_zone, -np.inf)



#     return {
#         'indices' : discords_idx,
#         'distances' : discords_dist,
#         'nn_indices' : discords_nn_idx
#         }

def top_k_discords(matrix_profile: dict, top_k: int = 3) -> dict:
    mp = matrix_profile['mp'].copy()
    mpi = matrix_profile['mpi']
    excl_zone = matrix_profile['excl_zone']
    m = matrix_profile['m']

    discords_idx = []
    discords_dist = []
    discords_nn_idx = []

    for _ in range(top_k):
        # Find the index of the maximum matrix profile value (discord candidate)
        discord_idx = np.argmax(mp)
        discord_dist = mp[discord_idx]
        nn_idx = int(mpi[discord_idx])

        # Stop if the maximum value is invalid (e.g., nan or negative)
        if discord_dist == -np.inf or np.isnan(discord_dist):
            break

        # Append the discord information to the results
        discords_idx.append(discord_idx)
        discords_dist.append(discord_dist)
        discords_nn_idx.append(nn_idx)

        # Apply exclusion zone to avoid trival matches around the found discord
        apply_exclusion_zone(mp, discord_idx, excl_zone, val=-np.inf)

    return {
        'indices': discords_idx,
        'distances': discords_dist,
        'nn_indices': discords_nn_idx
    }
