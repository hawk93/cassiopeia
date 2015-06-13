import cassiopeia.dto.requests
import cassiopeia.type.dto.summoner

# @param summoner_names # list<str> or str # The summoner name(s) to look up
# @return # dict<str, Summoner> # The requested summoners
def get_summoners_by_name(summoner_names):
    # Can only have 40 summoners max if it's a list
    if(isinstance(summoner_names, list) and len(summoner_names > 40)):
        raise ValueError("Can only get up to 40 summoners at once.")

    name_string = ",".join(str(x) for x in summoner_names) if isinstance(summoner_names, list) else str(summoner_names)

    # Get JSON response
    request = "{version}/summoner/by-name/{names}".format(version=cassiopeia.dto.requests.api_versions["summoner"], names=name_string)
    response = cassiopeia.dto.requests.get(request)

    # Convert response to Dto type
    for name, summoner in response.items():
        response[name] = cassiopeia.type.dto.summoner.Summoner(summoner)

    return response

# @param summoner_ids # list<int> or int # The summoner ID(s) to look up
# @return # dict<str, Summoner> # The requested summoners
def get_summoners_by_id(summoner_ids):
    # Can only have 40 summoners max if it's a list
    if(isinstance(summoner_ids, list) and len(summoner_ids > 40)):
        raise ValueError("Can only get up to 40 summoners at once.")

    id_string = ",".join(str(x) for x in summoner_ids) if isinstance(summoner_ids, list) else str(summoner_ids)

    # Get JSON response
    request = "{version}/summoner/{ids}".format(version=cassiopeia.dto.requests.api_versions["summoner"], ids=id_string)
    response = cassiopeia.dto.requests.get(request)

    # Convert response to Dto type
    for id_, summoner in response.items():
        response[id_] = cassiopeia.type.dto.summoner.Summoner(summoner)

    return response

# @param summoner_ids # list<int> or int # The summoner ID(s) to get mastery pages for
# @return # dict<str, MasteryPages> # The cassiopeia.dto.requests summoners' mastery pages
def get_summoner_masteries(summoner_ids):
    # Can only have 40 summoners max if it's a list
    if(isinstance(summoner_ids, list) and len(summoner_ids > 40)):
        raise ValueError("Can only get masteries for up to 40 summoners at once.")

    id_string = ",".join(str(x) for x in summoner_ids) if isinstance(summoner_ids, list) else str(summoner_ids)

    # Get JSON response
    request = "{version}/summoner/{ids}/masteries".format(version=cassiopeia.dto.requests.api_versions["summoner"], ids=id_string)
    response = cassiopeia.dto.requests.get(request)

    # Convert response to Dto type
    for id_, masteries in response.items():
        response[id_] = cassiopeia.type.dto.summoner.MasteryPages(masteries)

    return response

# @param summoner_ids # list<int> or int # The summoner ID(s) to get names for
# @return # dict<str, str> # The names of the requested summoners
def get_summoner_names(summoner_ids):
    # Can only have 40 summoners max if it's a list
    if(isinstance(summoner_ids, list) and len(summoner_ids > 40)):
        raise ValueError("Can only get names for up to 40 summoners at once.")

    id_string = ",".join(str(x) for x in summoner_ids) if isinstance(summoner_ids, list) else str(summoner_ids)

    # Get JSON response
    request = "{version}/summoner/{ids}/name".format(version=cassiopeia.dto.requests.api_versions["summoner"], ids=id_string)
    return cassiopeia.dto.requests.get(request)

# @param summoner_ids # list<int> or int # The summoner ID(s) to get rune pages for
# @return # dict<str, RunePages> # The cassiopeia.dto.requests summoners' rune pages
def get_summoner_runes(summoner_ids):
    # Can only have 40 summoners max if it's a list
    if(isinstance(summoner_ids, list) and len(summoner_ids > 40)):
        raise ValueError("Can only get runes for up to 40 summoners at once.")

    id_string = ",".join(str(x) for x in summoner_ids) if isinstance(summoner_ids, list) else str(summoner_ids)

    # Get JSON response
    request = "{version}/summoner/{ids}/runes".format(version=cassiopeia.dto.requests.api_versions["summoner"], ids=id_string)
    response = cassiopeia.dto.requests.get(request)

    # Convert response to Dto type
    for id_, runes in response.items():
        response[id_] = cassiopeia.type.dto.summoner.RunePages(runes)

    return response