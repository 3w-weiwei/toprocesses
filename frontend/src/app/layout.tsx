import { Inter } from "next/font/google";
import { NuqsAdapter } from "nuqs/adapters/next/app";
import { Toaster } from "sonner";
import "./globals.css";
// NOTE  MC8yOmFIVnBZMlhuam92bHFJSGxxSUU2YUVKWVZnPT06ZDYzY2JiZWY=

const inter = Inter({ subsets: ["latin"] });
// NOTE  MS8yOmFIVnBZMlhuam92bHFJSGxxSUU2YUVKWVZnPT06ZDYzY2JiZWY=

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="zh-CN"
      suppressHydrationWarning
    >
      <body
        className={inter.className}
        suppressHydrationWarning
      >
        <NuqsAdapter>{children}</NuqsAdapter>
        <Toaster />
      </body>
    </html>
  );
}
