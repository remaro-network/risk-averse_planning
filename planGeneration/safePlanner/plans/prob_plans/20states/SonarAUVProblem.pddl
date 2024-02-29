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
        t16Point - waypoint
        t17Point - waypoint
        t18Point - waypoint
        t19Point - waypoint
        t20Point - waypoint
    )

    (:init
        (at auv initialPoint)
        (ObjectAvoidanceFailure0 initialPoint oilLeakagePoint)
        (ObjectAvoidanceFailure0 oilLeakagePoint middlePoint)
        (ObjectAvoidanceFailure1 middlePoint middletoPoint)
        (ObjectAvoidanceFailure1 oilLeakagePoint finalPoint)
        (ObjectAvoidanceFailure1 oilLeakagePoint t16Point)
        (ObjectAvoidanceFailure1 t16Point finalPoint)
        (ObjectAvoidanceFailure2 oilLeakagePoint harmlessPoint)


    )

    (:goal
        (at auv finalPoint)
       ; (verticalInspection middlePoint)
        (pipelineInspection oilLeakagePoint)
        (pipelineInspection t7Point)
        (pipelineInspection t8Point)
        (pipelineInspection t9Point)
        (pipelineInspection t12Point)
        (pipelineInspection t17Point)
        ;(pipelineInspection t10Point)
        ;(pipelineInspection t11Point)
        (pipelineInspection t16Point)
       


    )

)
