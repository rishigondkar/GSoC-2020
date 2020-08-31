cmake_minimum_required(VERSION 2.6)
PROJECT(  conversationalAgent )

INCLUDE( $ENV{ROBOCOMP}/cmake/robocomp.cmake )

ROBOCOMP_IDSL_TO_ICE( CommonBehavior AGMCommonBehavior AGMExecutive AGMExecutiveTopic AGMWorldModel GenericBase InnerModelManager Laser OmniRobot Planning )
