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
        t7Point - waypoint
        t8Point - waypoint
        t9Point - waypoint
        t10Point - waypoint
        t11Point - waypoint
        t12Point - waypoint
        t13Point - waypoint
        t14Point - waypoint
        t15Point - waypoint
    )

    (:init
        (at auv initialPoint)
        (ObjectAvoidanceFailure0 initialPoint oilLeakagePoint)
        (ObjectAvoidanceFailure0 oilLeakagePoint middlePoint)
        (ObjectAvoidanceFailure1 middlePoint middletoPoint)
        (ObjectAvoidanceFailure0 t7Point t8Point)
        (ObjectAvoidanceFailure1 t8Point t9Point)
        (ObjectAvoidanceFailure3 t9Point tenPoint)
        (ObjectAvoidanceFailure0 t7Point t8Point)
        (ObjectAvoidanceFailure1 t8Point ninePoint)
        (ObjectAvoidanceFailure4 t10Point oilLeakagePoint)
        (ObjectAvoidanceFailure2 t11Point twelvePoint)
        (ObjectAvoidanceFailure1 t12Point oilLeakagePoint)
        (ObjectAvoidanceFailure3 oilLeakagePoint t13Point)
        (ObjectAvoidanceFailure2 t13Point t14Point)
        (ObjectAvoidanceFailure5 t14Point fiftheenPoint)
        (ObjectAvoidanceFailure2 t15Point oilLeakagePoint)
        (ObjectAvoidanceFailure5 oilLeakagePoint finalPoint)
        (ObjectAvoidanceFailure5 oilLeakagePoint harmlessPoint)


    )

    (:goal
        (at auv finalPoint)
        (verticalInspection middlePoint)
        (pipelineInspection oilLeakagePoint)
    )

    ;(:metric (maximize ()))
)
