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
        t41Point - waypoint
        t42Point - waypoint
        t43Point - waypoint
        t44Point - waypoint
        t45Point - waypoint
        t46Point - waypoint
        t47Point - waypoint
        t48Point - waypoint
        t49Point - waypoint
        t50Point - waypoint
        t51Point - waypoint
        t52Point - waypoint
        t53Point - waypoint
        t54Point - waypoint
        t55Point - waypoint
        t56Point - waypoint
        t57Point - waypoint
        t58Point - waypoint
        t59Point - waypoint
        t60Point - waypoint
        t61Point - waypoint
        t62Point - waypoint
        t63Point - waypoint
        t64Point - waypoint
        t65Point - waypoint
        t66Point - waypoint
        t67Point - waypoint
        t68Point - waypoint
        t69Point - waypoint
        t70Point - waypoint


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
        (pipelineInspection t41Point)
        (pipelineInspection t42Point)
        (pipelineInspection t43Point)
        (pipelineInspection t44Point)
        (pipelineInspection t45Point)
        (pipelineInspection t46Point)
        (pipelineInspection t47Point)
        (pipelineInspection t48Point)
        (pipelineInspection t49Point)
        (pipelineInspection t50Point)
        (pipelineInspection t51Point)
        (pipelineInspection t52Point)
        (pipelineInspection t53Point)
        (pipelineInspection t54Point)
        (pipelineInspection t55Point)
        (pipelineInspection t56Point)
        (pipelineInspection t57Point)
        (pipelineInspection t58Point)
        (pipelineInspection t59Point)
        (pipelineInspection t60Point)
        (pipelineInspection t61Point)
        (pipelineInspection t62Point)
        (pipelineInspection t63Point)
        (pipelineInspection t64Point)
        (pipelineInspection t65Point)
        (pipelineInspection t66Point)
        (pipelineInspection t67Point)
        (pipelineInspection t68Point)
        (pipelineInspection t69Point)
        (pipelineInspection t70Point)
    )

)
