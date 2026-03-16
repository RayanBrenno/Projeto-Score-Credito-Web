interface FormSectionProps {
  title: string;
  subtitle?: string;
  children: React.ReactNode;
}

export default function FormSection({ title, subtitle, children }: FormSectionProps) {
  return (
    <div className="mb-8 pb-8 border-b border-slate-700/50 last:border-b-0 last:mb-0 last:pb-0">
      <div className="mb-6">
        <h2 className="text-lg font-semibold text-white">{title}</h2>
        {subtitle && <p className="text-slate-400 text-sm mt-1">{subtitle}</p>}
      </div>
      {children}
    </div>
  );
}
