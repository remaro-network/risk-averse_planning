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
        t16Point - waypoint
        t17Point - waypoint
        t18Point - waypoint
        t19Point - waypoint
        t20Point - waypoint
        t21Point - waypoint
        t22Point - waypoint
        t23Point - waypoint
        t24Point - waypoint
        t25Point - waypoint
        t26Point - waypoint
        t27Point - waypoint
        t28Point - waypoint
        t29Point - waypoint
        t30Point - waypoint
        t31Point - waypoint
        t32Point - waypoint
        t33Point - waypoint
        t34Point - waypoint
        t35Point - waypoint
        t36Point - waypoint
        t37Point - waypoint
        t38Point - waypoint
        t39Point - waypoint
        t40Point - waypoint



    )

    (:init
        (at auv initialPoint)
        (ObjectAvoidanceFailure0 initialPoint oilLeakagePoint)
        (ObjectAvoidanceFailure0 oilLeakagePoint middlePoint)
        (ObjectAvoidanceFailure1 middlePoint middletoPoint)
        (ObjectAvoidanceFailure1 oilLeakagePoint finalPoint)
        (ObjectAvoidanceFailure2 oilLeakagePoint harmlessPoint)
        (ObjectAvoidanceFailure0 t10Point oilLeakagePoint)
        (ObjectAvoidanceFailure0 t11Point oilLeakagePoint)
        (ObjectAvoidanceFailure2 oilLeakagePoint t12Point)
        (ObjectAvoidanceFailure2 oilLeakagePoint t13Point)
        (ObjectAvoidanceFailure2 oilLeakagePoint t14Point)
        (ObjectAvoidanceFailure2 oilLeakagePoint t15Point)
        (ObjectAvoidanceFailure2 oilLeakagePoint t16Point)
        (ObjectAvoidanceFailure2 oilLeakagePoint t17Point)
        (ObjectAvoidanceFailure2 oilLeakagePoint t18Point)
        (ObjectAvoidanceFailure2 oilLeakagePoint t19Point)


    )

    (:goal
        (at auv finalPoint)
        (pipelineInspection oilLeakagePoint)
        (pipelineInspection t7Point)
        (pipelineInspection t8Point)
        (pipelineInspection t9Point)
        (pipelineInspection t10Point)
        (pipelineInspection t11Point)
        (pipelineInspection t12Point)
        (pipelineInspection t16Point)
        (pipelineInspection t17Point)
        (pipelineInspection t18Point)
        (pipelineInspection t19Point)
        (pipelineInspection t20Point)
        (pipelineInspection t21Point)
        (pipelineInspection t22Point)
        (pipelineInspection t23Point)
        (pipelineInspection t24Point)
        (pipelineInspection t25Point)
        (pipelineInspection t26Point)
        (pipelineInspection t27Point)
        (pipelineInspection t28Point)
        (pipelineInspection t29Point)
        (pipelineInspection t30Point)
        (pipelineInspection t31Point)
        (pipelineInspection t32Point)
        (pipelineInspection t33Point)
        (pipelineInspection t34Point)
        (pipelineInspection t35Point)
        (pipelineInspection t36Point)
        (pipelineInspection t37Point)
        (pipelineInspection t38Point)
        (pipelineInspection t39Point)
        (pipelineInspection t40Point)

    )

)
