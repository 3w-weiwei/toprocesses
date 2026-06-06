import { cn } from "@/lib/utils";
// @ts-expect-error  MC8yOmFIVnBZMlhuam92bHFJSGxxSUU2V1VOWFdnPT06MjM2NDA4MTM=

function Skeleton({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn("animate-pulse rounded-md bg-muted", className)}
      {...props}
    />
  );
}

export { Skeleton };
// @ts-expect-error  MS8yOmFIVnBZMlhuam92bHFJSGxxSUU2V1VOWFdnPT06MjM2NDA4MTM=
