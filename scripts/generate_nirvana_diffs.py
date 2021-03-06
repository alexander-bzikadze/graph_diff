import logging
import os

from graph_diff.baseline_algorithm import BaselineAlgorithm
from graph_diff.nirvana_object_model.pipeline import Pipeline
from graph_diff.nirvana_object_model.worflow_generator.similar_workflow_generator import SimilarWorkflowGenerator
from graph_diff.nirvana_object_model.workflow_to_graph_converter.complete_workflow_to_graph_converter import \
    CompleteWorkflowToGraphConverter

NUMBER_OF_TESTS = 100

# Algo = Algorithm()

Algo = BaselineAlgorithm()
# DIRECTORY = "../nirvana_diffs_simple/"
# converter = SimpleWorkflowToGraphConverter()

converter = CompleteWorkflowToGraphConverter()
DIRECTORY = '../nirvana_diffs/'

if not os.path.exists(DIRECTORY):
    logging.info('Creating directory {0}'.format(DIRECTORY))
    os.makedirs(DIRECTORY)

logging.info('Starting series of {} pipeline tests, results to {}'.format(NUMBER_OF_TESTS, DIRECTORY))
logging.info('Used converter is {}'.format(type(converter).__class__.__name__))

for i in range(0, NUMBER_OF_TESTS):
    logging.info('Running test {}'.format(i))
    logging.debug('Generation two workflows')
    # generator = StandardWorkflowGenerator().generate_blocks()
    generator = SimilarWorkflowGenerator()
    # generator = ChainWorkflowGenerator().generate_blocks(chain_number=1)
    workflow1 = generator.generate_workflow()
    workflow2 = generator.generate_workflow()

    logging.debug('Running pipeline on two generated workflows')
    Pipeline(
        algorithm=Algo,
        workflow_converter=converter
    ).print_diff(workflow1=workflow1, workflow2=workflow2, path=DIRECTORY + str(i) + '.png')

    logging.info("Test i={0} of n={1} done.".format(i, NUMBER_OF_TESTS))
