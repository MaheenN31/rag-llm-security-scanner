export type Severity = "Critical" | "High" | "Medium" | "Low" | "Info";

export type HealthResponse = {
  status: string;
  app_name: string;
  environment: string;
};

export type ScanSummary = {
  totalProbes: number;
  passed: number;
  failed: number;
  riskScore: number;
  criticalFindings: number;
};

export type Finding = {
  id: string;
  severity: Severity;
  probeName: string;
  owaspCategory: string;
  evidence: string;
  recommendation: string;
};