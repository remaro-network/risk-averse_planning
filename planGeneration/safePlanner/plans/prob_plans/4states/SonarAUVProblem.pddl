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

    )

    (:init
        (at auv initialPoint)
        (ObjectAvoidanceFailure0 initialPoint oilLeakagePoint)
        (ObjectAvoidanceFailure1 oilLeakagePoint finalPoint)
        (ObjectAvoidanceFailure2 oilLeakagePoint harmlessPoint)


    )

    (:goal
        (at auv finalPoint)
        (pipelineInspection oilLeakagePoint)
    )

    ;(:metric (maximize ()))
)
