import os
import logging
from .environment_parser import extract_environment_requirement
from .dependency_parser import extract_dependencies
from .doc_parser import match_doc

def parser(project_path):
    """
    The parsing module of CXXCrafter.
    args:
        + project_path
    
    """
    logger = logging.getLogger(__name__)

    if not os.path.exists(project_path):
        logger.info("Wroing project path!")
        
    project_name = os.path.basename(project_path)
    environment_requirement = extract_environment_requirement(project_path)
    dependencies = extract_dependencies(project_path)
    try: 
        docs = match_doc(project_path)
    except Exception as e:
        logger.error(e)
        docs = ""
    return project_name, project_path, environment_requirement, dependencies, docs
