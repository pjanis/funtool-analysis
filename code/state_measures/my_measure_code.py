
import funtool.state_measure
import numbers

def all_ratios(state_measure, analysis_collection, state_collection, overriding_parameters=None):
    measure_parameters = funtool.state_measure.get_measure_parameters(state_measure, overriding_parameters)
    all_measures= list(analysis_collection.state.measures.keys())
    for idx,first_measure in enumerate(all_measures):
        if isinstance(analysis_collection.state.measures[first_measure],numbers.Number):
            for second_measure in all_measures[(idx+1):-1]:
                if isinstance(analysis_collection.state.measures[second_measure],numbers.Number):
                    a_value= analysis_collection.state.measures[first_measure]
                    b_value= analysis_collection.state.measures[second_measure]
                    analysis_collection.state.measures[first_measure+"_to_"+second_measure]= funtool.state_measures.default._compute_ratio(a_value,b_value)
    return analysis_collection

@funtool.state_measure.state_and_parameter_measure
def number_of_scripts(state,parameters):
    return len(state_scripts(state))

#duplicate of function in funtool_scratch_processes.state_measures.default
def state_scripts(state):   
    json_data= state.data.get('json')
    scripts=[]
    if json_data != None:
        scripts.extend(json_data.get('scripts',[]))
        for child in json_data.get('children'):
            scripts.extend(child.get('scripts',[]))
    return scripts
