# RELION optimiser; version 3.0.7
# --o Refine3D/job020/run --auto_refine --split_random_halves --i Class2D/job017/run_it025_data.star --ref InitialModel/job019/from_relion2_job144_resampled.mrc --firstiter_cc --ini_high 20 --dont_combine_weights_via_disc --pool 3 --pad 2 --particle_diameter 1000 --flatten_solvent --zero_mask --oversampling 1 --healpix_order 3 --auto_local_healpix_order 4 --offset_range 5 --offset_step 2 --sym I2 --low_resol_join_halves 40 --norm --scale --j 3 --gpu  

data_optimiser_general

_rlnOutputRootName                                    Refine3D/job020/run
_rlnModelStarFile                                     Refine3D/job020/run_it013_half1_model.star
_rlnModelStarFile2                                    Refine3D/job020/run_it013_half2_model.star
_rlnExperimentalDataStarFile                          Refine3D/job020/run_it013_data.star
_rlnOrientSamplingStarFile                            Refine3D/job020/run_it013_sampling.star
_rlnCurrentIteration                                            13
_rlnNumberOfIterations                                         999
_rlnDoSplitRandomHalves                                          1
_rlnJoinHalvesUntilThisResolution                        40.000000
_rlnAdaptiveOversampleOrder                                      1
_rlnAdaptiveOversampleFraction                            0.999000
_rlnRandomSeed                                          1581722818
_rlnParticleDiameter                                   1000.000000
_rlnWidthMaskEdge                                                5
_rlnDoZeroMask                                                   1
_rlnDoSolventFlattening                                          1
_rlnDoSolventFscCorrection                                       0
_rlnSolventMaskName                                   None
_rlnSolventMask2Name                                  None
_rlnBodyStarFile                                      None
_rlnTauSpectrumName                                   None
_rlnCoarseImageSize                                             68
_rlnMaximumCoarseImageSize                                     512
_rlnHighresLimitExpectation                               -1.00000
_rlnIncrementImageSize                                          16
_rlnDoMapEstimation                                              1
_rlnDoFastSubsetOptimisation                                     0
_rlnDoStochasticGradientDescent                                  0
_rlnSgdInitialIterations                                        50
_rlnSgdFinalIterations                                          50
_rlnSgdInBetweenIterations                                     200
_rlnSgdInitialResolution                                 35.000000
_rlnSgdFinalResolution                                   15.000000
_rlnSgdInitialSubsetSize                                       100
_rlnSgdFinalSubsetSize                                         500
_rlnSgdMuFactor                                           0.000000
_rlnSgdSigma2FudgeInitial                                 8.000000
_rlnSgdSigma2FudgeHalflife                                      -1
_rlnSgdSkipAnneal                                                0
_rlnSgdSubsetSize                                               -1
_rlnSgdWriteEverySubset                                          1
_rlnSgdStepsize                                           0.500000
_rlnDoAutoRefine                                                 1
_rlnAutoLocalSearchesHealpixOrder                                4
_rlnNumberOfIterWithoutResolutionGain                            5
_rlnBestResolutionThusFar                                 0.052669
_rlnNumberOfIterWithoutChangingAssignments                       1
_rlnDoSkipAlign                                                  0
_rlnDoSkipRotate                                                 0
_rlnOverallAccuracyRotations                              2.767000
_rlnOverallAccuracyTranslations                           1.874000
_rlnChangesOptimalOrientations                            1.591668
_rlnChangesOptimalOffsets                                 0.565289
_rlnChangesOptimalClasses                                 0.000000
_rlnSmallestChangesOrientations                           1.511807
_rlnSmallestChangesOffsets                                0.517576
_rlnSmallestChangesClasses                                       0
_rlnLocalSymmetryFile                                 None
_rlnDoHelicalRefine                                              0
_rlnIgnoreHelicalSymmetry                                        0
_rlnHelicalTwistInitial                                   0.000000
_rlnHelicalRiseInitial                                    0.000000
_rlnHelicalCentralProportion                              0.300000
_rlnHelicalMaskTubeInnerDiameter                          -1.00000
_rlnHelicalMaskTubeOuterDiameter                          -1.00000
_rlnHelicalSymmetryLocalRefinement                               0
_rlnHelicalSigmaDistance                                  -1.00000
_rlnHelicalKeepTiltPriorFixed                                    0
_rlnHasConverged                                                 0
_rlnHasHighFscAtResolLimit                                       0
_rlnHasLargeSizeIncreaseIterationsAgo                            0
_rlnDoCorrectNorm                                                1
_rlnDoCorrectScale                                               1
_rlnDoCorrectCtf                                                 0
_rlnDoRealignMovies                                              0
_rlnDoIgnoreCtfUntilFirstPeak                                    0
_rlnCtfDataArePhaseFlipped                                       0
_rlnCtfDataAreCtfPremultiplied                                   0
_rlnDoOnlyFlipCtfPhases                                          0
_rlnRefsAreCtfCorrected                                          0
_rlnFixSigmaNoiseEstimates                                       0
_rlnFixSigmaOffsetEstimates                                      0
_rlnMaxNumberOfPooledParticles                                   9
 
