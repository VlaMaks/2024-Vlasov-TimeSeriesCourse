import numpy as np

from modules.utils import *


# def top_k_motifs(matrix_profile: dict, top_k: int = 3) -> dict:
#     """
#     Find the top-k motifs based on matrix profile

#     Parameters
#     ---------
#     matrix_profile: the matrix profile structure
#     top_k : number of motifs

#     Returns
#     --------
#     motifs: top-k motifs (left and right indices and distances)
#     """

#     motifs_idx = []
#     motifs_dist = []

#     # INSERT YOUR CODE

#     # Extract matrix profile and associated parameters
#     mp = matrix_profile['mp']
#     mpi = matrix_profile['mpi']
#     exclusion_zone = matrix_profile.get('excl_zone', 0)
#     m = matrix_profile['m']


#     # Copy matrix profile to modify it without affecting the original
#     mp_copy = mp.copy()

#     for _ in range(top_k):
#         # Find the minimum distance in the matrix profile
#         min_idx = np.argmin(mp)
#         min_dist = mp[min_idx]

#         # Break if all remaining distances are infinite (no more motifs to find)
#         if np.isinf(min_dist):
#             break

#         # Find indices of the motif pair
#         left_idx = min_idx
#         right_idx = int(mpi[min_idx])

#         # Add the motif to the result
#         motifs_idx.append((left_idx, right_idx))
#         motifs_dist.append(min_dist)

#         # Apply exclusion zone to avoid trivial matches
#         mp_copy = apply_exclusion_zone(mp_copy, left_idx, exclusion_zone, np.inf)
#         mp_copy = apply_exclusion_zone(mp_copy, right_idx, exclusion_zone, np.inf)

#     return {
#         "indices" : motifs_idx,
#         "distances" : motifs_dist
#         }

def top_k_motifs(matrix_profile: dict, top_k: int = 3) -> dict:
    """
    Find the top-k motifs based on matrix profile.

    Parameters
    ----------
    matrix_profile: dict
        The matrix profile structure containing the 'mp' and 'mpi'.
    top_k: int
        Number of motifs to find.

    Returns
    -------
    dict
        A dictionary containing 'motifs_idx' (indices of motifs) 
        and 'motifs_dist' (distances of motifs).
    """
    # Extract matrix profile and related data
    mp = matrix_profile['mp'].copy()  # Copy to modify
    mpi = matrix_profile['mpi']
    excl_zone = matrix_profile['excl_zone']
    m = matrix_profile['m']

    motifs_idx = []
    motifs_dist = []

    for _ in range(top_k):
      
        
        # Find the index of the minimum value in the matrix profile
        min_idx = np.argmin(mp)
        min_dist = mp[min_idx]
        
        # Save the pair of motifs
        second_idx = int(mpi[min_idx])
        motifs_idx.append((min_idx, second_idx))
        motifs_dist.append(min_dist)
        
        # Apply the exclusion zone to both indices
        mp = apply_exclusion_zone(mp, min_idx, excl_zone, np.inf)
        mp = apply_exclusion_zone(mp, second_idx, excl_zone, np.inf)

    return {'indices': motifs_idx, 'distances': motifs_dist}



