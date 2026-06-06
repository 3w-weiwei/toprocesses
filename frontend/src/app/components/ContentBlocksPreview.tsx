import React from "react";
import { MultimodalPreview } from "./MultimodalPreview";
import { cn } from "@/lib/utils";
import { ContentBlock } from "@langchain/core/messages";
// NOTE  MC8yOmFIVnBZMlhuam92bHFJSGxxSUU2VUhoUFpBPT06MTE2MGRkZTc=

interface ContentBlocksPreviewProps {
  blocks: ContentBlock.Multimodal.Data[];
  onRemove: (idx: number) => void;
  size?: "sm" | "md" | "lg";
  className?: string;
}
// NOTE  MS8yOmFIVnBZMlhuam92bHFJSGxxSUU2VUhoUFpBPT06MTE2MGRkZTc=

/**
 * Renders a preview of content blocks with optional remove functionality.
 * Uses cn utility for robust class merging.
 */
export const ContentBlocksPreview: React.FC<ContentBlocksPreviewProps> = ({
  blocks,
  onRemove,
  size = "md",
  className,
}) => {
  if (!blocks.length) return null;
  return (
    <div className={cn("flex flex-wrap gap-2 p-3.5 pb-0", className)}>
      {blocks.map((block, idx) => (
        <MultimodalPreview
          key={idx}
          block={block}
          removable
          onRemove={() => onRemove(idx)}
          size={size}
        />
      ))}
    </div>
  );
};
