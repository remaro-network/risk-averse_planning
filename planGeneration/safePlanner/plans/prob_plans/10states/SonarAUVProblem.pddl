(define (problem ObstacleAvoidanceSonarAUV)
    (:domain sonarAUV)
    (:objects
        auv - robot
        SSSsonar0 - sonar0
        SSSsonar1 - sonar1
        initialPoint - waypoint
        finalPoint - waypoint
        oilLeakagePoint - waypoint
        harmlessPoint - waypoint
        middlePoint - waypoint
        middletoPoint - waypoint
        sevenPoint - waypoint
        eightPoint - waypoint
        ninePoint - waypoint
        tenPoint - waypoint


    )

    (:init
        (at auv initialPoint)
        (ObjectAvoidanceFailure0 initialPoint oilLeakagePoint)
        (ObjectAvoidanceFailure0 oilLeakagePoint middlePoint)
        (ObjectAvoidanceFailure1 middlePoint middletoPoint)
        (ObjectAvoidanceFailure0 middletoPoint sevenPoint)
        (ObjectAvoidanceFailure0 sevenPoint eightPoint)
        (ObjectAvoidanceFailure1 eightPoint ninePoint)
        (ObjectAvoidanceFailure3 ninePoint tenPoint)
        (ObjectAvoidanceFailure3 oilLeakagePoint finalPoint)
        (ObjectAvoidanceFailure2 oilLeakagePoint harmlessPoint)


    )

    (:goal
        (at auv finalPoint)
        (verticalInspection middlePoint)
        (pipelineInspection oilLeakagePoint)
    )

)
