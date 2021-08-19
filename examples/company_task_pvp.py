# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
To add a new task to PET, both a DataProcessor and a PVP for this task must
be added. The PVP is responsible for applying patterns to inputs and mapping
labels to their verbalizations (see the paper for more details on PVPs).
This file shows an example of a PVP for a new task.
"""

from typing import List

from pet.pvp import PVP, PVPS, FilledPattern
from pet.utils import InputExample

class CompanyClassificationPVP(PVP):
    """
    Example for a pattern-verbalizer pair (PVP).
    """

    # Set this to the name of the task
    TASK_NAME = "company"

    # Set this to the verbalizer for the given task: a mapping from the task's labels (which can be obtained using
    # the corresponding DataProcessor's get_labels method) to tokens from the language model's vocabulary
    VERBALIZER = {
        "1": ["Robotik"],
        "2": ["Forschung", "Research"],
        "3": ["Künstliche Intelligenz", "Artificial Intelligence"],
        "4": ["Simulation"]
    }

    def get_parts(self, example: InputExample) -> FilledPattern:
        text = self.shortenable(example.text_a)

        if self.pattern_id == 0:
            return [self.mask, ':', text], []
        elif self.pattern_id == 1:
            return [self.mask, 'News:', text], []
        elif self.pattern_id == 2:
            return ['[ Category:', self.mask, ']', text], []
        elif self.pattern_id == 3:
            return [self.mask, '-', text], []
        else:
            raise ValueError("No pattern implemented for id {}".format(self.pattern_id))

    def verbalize(self, label) -> List[str]:
        return CompanyClassificationPVP.VERBALIZER[label]


# register the PVP for this task with its name
PVPS[CompanyClassificationPVP.TASK_NAME] = CompanyClassificationPVP
