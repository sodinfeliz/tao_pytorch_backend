# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
#
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

"""Initial module."""
# flake8: noqa: F401, F403
from .basepruner import LocalPruner, GlobalPruner
from .magnitude_based_pruner import LocalMagnitudePruner, GlobalMagnitudePruner
from .batchnorm_scale_pruner import LocalBNScalePruner, GlobalBNScalePruner
from .structural_reg_pruner import LocalStructrualRegularizedPruner
from .structural_dropout_pruner import StructrualDropoutPruner
