import wave as wave
import pyroomacoustics as pa
import numpy as np

pa.datasets.CMUArcticCorpus(basedir='./CMU_ARCTIC',
                            download=True, speaker=['aew', 'axb'])
