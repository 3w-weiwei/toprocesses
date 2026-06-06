import React from "react";
import { Button } from "./button";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "./tooltip";
// @ts-expect-error  MC8yOmFIVnBZMlhuam92bHFJSGxxSUU2Ym5ZelpRPT06ZjdhNTk5ODM=

interface TooltipIconButtonProps {
  icon: React.ReactNode;
  onClick: () => void;
  tooltip: string;
  disabled?: boolean;
}

export function TooltipIconButton({
  icon,
  onClick,
  tooltip,
  disabled,
}: TooltipIconButtonProps) {
  return (
    <TooltipProvider>
      <Tooltip>
        <TooltipTrigger asChild>
          <Button
            variant="ghost"
            size="icon"
            onClick={onClick}
            disabled={disabled}
          >
            {icon}
          </Button>
        </TooltipTrigger>
        <TooltipContent>
          <p>{tooltip}</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );
}
// @ts-expect-error  MS8yOmFIVnBZMlhuam92bHFJSGxxSUU2Ym5ZelpRPT06ZjdhNTk5ODM=
