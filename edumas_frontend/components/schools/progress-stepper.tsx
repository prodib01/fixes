"use client";

import { Check } from "lucide-react";
import { cn } from "@/lib/utils";

interface Step {
  id: number;
  name: string;
  description: string;
}

interface ProgressStepperProps {
  steps: Step[];
  currentStep: number;
  completedSteps: number[];
}

export function ProgressStepper({
  steps,
  currentStep,
  completedSteps,
}: ProgressStepperProps) {
  return (
    <div className="flex flex-col space-y-0">
      {steps.map((step, index) => {
        const isCompleted = completedSteps.includes(step.id);
        const isCurrent = currentStep === step.id;
        const isLast = index === steps.length - 1;

        return (
          <div key={step.id} className="relative">
            <div className="flex items-start">
              <div className="flex flex-col items-center">
                <div
                  className={cn(
                    "flex h-10 w-10 items-center justify-center rounded-full border-2 transition-all duration-300",
                    isCompleted
                      ? "border-green-500 bg-green-500 text-white"
                      : isCurrent
                      ? "border-primary bg-primary text-white"
                      : "border-gray-300 bg-white text-gray-300"
                  )}
                >
                  {isCompleted ? (
                    <Check className="h-6 w-6" />
                  ) : (
                    <span className="text-sm font-medium">{step.id}</span>
                  )}
                </div>
                {!isLast && (
                  <div
                    className={cn(
                      "h-12 w-0.5 transition-all duration-500",
                      isCompleted ? "bg-green-500" : "bg-gray-300"
                    )}
                  />
                )}
              </div>
              <div className="ml-4 mt-1">
                <h3
                  className={cn(
                    "text-sm font-medium transition-colors duration-300",
                    isCompleted
                      ? "text-green-600"
                      : isCurrent
                      ? "text-primary font-semibold"
                      : "text-gray-500"
                  )}
                >
                  {step.name}
                </h3>
                <p
                  className={cn(
                    "text-xs transition-colors duration-300",
                    isCompleted || isCurrent ? "text-gray-600" : "text-gray-400"
                  )}
                >
                  {step.description}
                </p>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}
