(define (domain sonarAUV)
    (:requirements :typing :strips :equality :negative-preconditions :conditional-effects :probabilistic-effects  :disjunctive-preconditions) 

    (:types 
        waypoint robot robotPart - object
        sonar0 sonar1- robotPart
    )

    (:predicates
        (at ?auv - robot ?wp - waypoint)
        (outOfRangeSonar0 ?part - sonar0)
        (outOfRangeSonar1 ?part - sonar1)
        (pipelineInspection ?wp - waypoint)
        (verticalInspection ?wp - waypoint)
        (ObjectAvoidanceFailure0 ?from - waypoint ?to - waypoint)
        (ObjectAvoidanceFailure1 ?from - waypoint ?to - waypoint)
        (ObjectAvoidanceFailure2 ?from - waypoint ?to - waypoint)

    )

    (:action obstacle-avoidance
        :parameters (
            ?auv - robot
            ?wp - waypoint
            ?sonar0 - sonar0
        )
        :precondition (and 
            (at ?auv ?wp)
            (not (outOfRangeSonar0 SSSsonar0))
        )
        :effect (and 
            (probabilistic 
                ; 90% chance to inspect and report suspicious area
                0.9 (pipelineInspection ?wp)
            )
           ; (probabilistic 
                ; 95% chance to inspect and report suspicious area
            ;    0.95 (verticalInspection ?wp)
            ;)
        )
    )

    (:action waypoint-following
        :parameters (
            ?auv - robot
            ?from - waypoint
            ?to - waypoint
            ?sonar1 - sonar1
            ?sonar0 - sonar0
        )
        :precondition (and 
            (at ?auv ?from)
            (not (outOfRangeSonar1 SSSsonar1))
        )
        :effect (and 
            (when (not (ObjectAvoidanceFailure1 ?from ?to)) (and
                (not (at ?auv ?from))   ; move from first to second waypoint
                (at ?auv ?to)
                )
            )
            ; on risky paths, sonar sensor cannot work functionality
            (probabilistic 
                0.95 (when (ObjectAvoidanceFailure0 ?from ?to) (outOfRangeSonar0 ?sonar0))
            )
            (probabilistic
                0.95 (when (ObjectAvoidanceFailure1 ?from ?to) (outOfRangeSonar1 ?sonar1))
            )
            (probabilistic
                0.5 (when (ObjectAvoidanceFailure2 ?from ?to) (outOfRangeSonar1 ?sonar1))
            )
            
        )
    )
)
