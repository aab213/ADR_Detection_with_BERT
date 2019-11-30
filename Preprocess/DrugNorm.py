
# coding: utf-8

# # DrugNorm
#
# author -- AR Dirkson --
#
# date -- 08-02-2019 --
#
# python version -- 3 --
#
# This script  first subsets the dictionary for the drug names that are in your corpus and then uses simple matching to replace them by the generic drug name chosen as a key in the dictionary.
#
# The CELEX_lwrd_unique is a list of all the unique lowercased words in the CELEX. Alternatives can be used but must be in list form for this script.
#
# Data input needs to be tokenized and the module only deals with lowercased words!
#
#

import pickle
from nltk import word_tokenize


class DrugNorm ():

    def __init__(self):
        pass

    #to use this function the files need to be sorted in the same folder as the script under /obj_lex/
    def load_obj(self, name):
        with open('obj_lex/' + name + '.pkl', 'rb') as f:
            return pickle.load(f, encoding='latin1')

    def subset_drug_normalize_dict (self, msgs):
        drug_norm_dict = self.load_obj('drug_normalize_dict')

        #subset the dictionary for the drug names actually used in the data
        alt_names_flat = [item for sublist in list(drug_norm_dict.values()) for item in sublist]
        set_drug = set(alt_names_flat)
        msgs_flat = [item for sublist in msgs for item in sublist]
        set_msgs = set (msgs_flat)

        inters_drug_msgs = set_drug.intersection(set_msgs)

        #remove all words from the drug normalization subset that are generic words in the CELEX using a set operation
        #lex_normal= self.load_obj ('celex_lwrd_unique')

        #lex_normal2 = list(lex_normal)
        #lex_normal_set = set(lex_normal2)

        #inters_drug_msgs_remove= lex_normal_set.intersection(inters_drug_msgs)

        #inters_drug_msgs_new = []

        #for word in inters_drug_msgs:
        #     if word not in inters_drug_msgs_remove:
        #            inters_drug_msgs_new.append(word)

        inters_drug_msgs_new2 = []

        for a, word in enumerate (inters_drug_msgs):
            if len(word) > 2:
                inters_drug_msgs_new2.append(word)

        drug_norm_dict_small = {}

        for key, value in drug_norm_dict.items():
            temp = []
            for word in value:
                if word == 'tomorrow':
                    continue
                elif word in inters_drug_msgs_new2:
                    temp.append(word)
            drug_norm_dict_small[key] = temp

        #Remove all keys with an empty list
        list_of_kept_keys = []

        for key,value in drug_norm_dict_small.items():
            if value != []:
                list_of_kept_keys.append(key)

        drug_norm_subdict_small = {k: drug_norm_dict_small[k] for k in (list_of_kept_keys)}

        return drug_norm_subdict_small, inters_drug_msgs_new2

    #normalization
    def drug_normalize (self, msgs):
        drug_norm_dict, inters_drug_msgs = self.subset_drug_normalize_dict (msgs)
        msgs2 = []
        total_cnt = []
        replaced = []
        replaced_with  = []
        for post in msgs:
            cnt = 0
            for a, word in enumerate (post):
                if word in inters_drug_msgs:
                    for key, value in drug_norm_dict.items ():
                        if word in value:
                            cnt += 1
                            txt = word.replace (word, key)
                            replaced.append (word)
                            replaced_with.append (key)
                            post[a] = txt
            total_cnt.append (cnt)
            msgs2.append(post)
        return msgs2, total_cnt, replaced, replaced_with
