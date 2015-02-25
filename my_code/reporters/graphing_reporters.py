
import funtool.reporter
import matplotlib.pyplot
import matplotlib.colors
import os

def scatter_plot(reporter,state_collection,overriding_parameters=None,logging=None):
    colors = list(matplotlib.colors.cnames.keys())
    reporter_parameters= funtool.reporter.get_parameters(reporter,overriding_parameters)
    reporter_parameters= set_default_parameters({'file_type':'png'},reporter_parameters)

    save_path= funtool.reporter.get_default_save_path(reporter_parameters)
    if not os.path.exists(save_path): os.makedirs(save_path)

    if not _can_write(reporter_parameters):
        raise funtool.reporter.ReporterError("Can't write to %s at %s" % (reporter_parameters['filename'], reporter_parameters['save_directory'] ))
   
    path_and_filename= os.path.join(save_path,".".join([reporter_parameters['filename'], reporter_parameters['file_type']]))

    x_value= reporter_parameters.get("x_value")
    y_value= reporter_parameters.get("y_value")
    default_value= reporter_parameters.get("default_value",0)
        
    if x_value != None and y_value != None:
        for index,group in enumerate(state_collection.groups_dict.get(reporter_parameters['series_grouping'],[])):
            for state in group.states:
                x=state.measures.get(x_value,default_value)
                y=state.measures.get(y_value,default_value)
                matplotlib.pyplot.scatter(x,y,c=colors[index])
    matplotlib.pyplot.savefig(path_and_filename)          

    return state_collection


def set_default_parameters(default_parameters, current_parameters): #adds missing default parameters
    default_copy= default_parameters.copy()
    default_copy.update(current_parameters)
    return default_copy

def _can_write(reporter_parameters):
    path_and_filename=  os.path.join(reporter_parameters['save_directory'],".".join([reporter_parameters['filename'], reporter_parameters['file_type']]))
    return os.path.exists(reporter_parameters['save_directory']) and ( not os.path.exists(path_and_filename) or reporter_parameters['overwrite'] )

