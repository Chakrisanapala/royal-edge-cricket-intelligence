import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api, Batter } from '../services/api';
import { Search, Filter, ArrowUpDown, ChevronRight, Info, CheckCircle2 } from 'lucide-react';

export const BattingAnalytics: React.FC = () => {
  const navigate = useNavigate();
  const [batters, setBatters] = useState<Batter[]>([]);
  const [loading, setLoading] = useState(true);
  const [roleFilter, setRoleFilter] = useState('All');
  const [search, setSearch] = useState('');
  const [sortBy, setSortBy] = useState('bpri_score');
  const [ascending, setAscending] = useState(false);

  useEffect(() => {
    loadBatters();
  }, [roleFilter, sortBy, ascending]);

  const loadBatters = () => {
    setLoading(true);
    api.getBatters(roleFilter === 'All' ? undefined : roleFilter, search || undefined, sortBy, ascending)
      .then(res => {
        setBatters(res);
        setLoading(false);
      });
  };

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    loadBatters();
  };

  const handleSort = (field: string) => {
    if (sortBy === field) {
      setAscending(!ascending);
    } else {
      setSortBy(field);
      setAscending(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Header and Controls */}
      <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="px-2.5 py-0.5 rounded bg-[#EB107E]/20 text-[#EB107E] text-[10px] font-bold uppercase">
              Audited Official Rankings
            </span>
            <span className="text-xs text-gray-400">SupeRR Selector Season 2</span>
          </div>
          <h2 className="text-xl font-bold text-white mt-1">Batting Pressure Reliability Index (BPRI)</h2>
          <p className="text-xs text-gray-400 mt-0.5">
            Composite weighting: 35% HP Strike Rate + 25% HP Average + 20% Death SR + 10% Chase SR + 10% Leverage Delta.
          </p>
        </div>

        {/* Search & Filters */}
        <div className="flex flex-wrap items-center gap-3">
          {/* Role Filter */}
          <div className="flex items-center gap-2 bg-[#122131] border border-white/10 rounded-lg px-3 py-1.5 text-xs">
            <Filter className="w-3.5 h-3.5 text-gray-400" />
            <select
              value={roleFilter}
              onChange={(e) => setRoleFilter(e.target.value)}
              className="bg-transparent text-white focus:outline-none text-xs cursor-pointer"
            >
              <option value="All" className="bg-[#0D1C2D]">All Roles</option>
              <option value="Finisher" className="bg-[#0D1C2D]">Finisher</option>
              <option value="Power Hitter" className="bg-[#0D1C2D]">Power Hitter</option>
              <option value="Middle-order" className="bg-[#0D1C2D]">Middle-order</option>
            </select>
          </div>

          {/* Search Bar */}
          <form onSubmit={handleSearch} className="relative">
            <Search className="w-3.5 h-3.5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="Search player or team..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="bg-[#122131] border border-white/10 rounded-lg pl-8 pr-3 py-1.5 text-xs text-white placeholder-gray-400 focus:outline-none focus:border-[#EB107E] w-48"
            />
          </form>
        </div>
      </div>

      {/* Batters Table */}
      <div className="bg-[#0D1C2D] border border-white/10 rounded-xl overflow-hidden shadow-xl">
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-[#122131] border-b border-white/10 text-[11px] font-bold text-gray-300 uppercase tracking-wider">
                <th className="py-3 px-4 w-12 text-center">Rank</th>
                <th className="py-3 px-4">Player / Franchise</th>
                <th 
                  className="py-3 px-4 cursor-pointer hover:text-white"
                  onClick={() => handleSort('bpri_score')}
                >
                  <div className="flex items-center gap-1 text-[#EB107E]">
                    BPRI Score <ArrowUpDown className="w-3 h-3" />
                  </div>
                </th>
                <th 
                  className="py-3 px-4 cursor-pointer hover:text-white"
                  onClick={() => handleSort('pressure_strike_rate')}
                >
                  <div className="flex items-center gap-1">
                    HP SR <ArrowUpDown className="w-3 h-3" />
                  </div>
                </th>
                <th 
                  className="py-3 px-4 cursor-pointer hover:text-white"
                  onClick={() => handleSort('pressure_batting_avg')}
                >
                  <div className="flex items-center gap-1">
                    HP Avg <ArrowUpDown className="w-3 h-3" />
                  </div>
                </th>
                <th 
                  className="py-3 px-4 cursor-pointer hover:text-white"
                  onClick={() => handleSort('death_strike_rate')}
                >
                  <div className="flex items-center gap-1">
                    Death SR <ArrowUpDown className="w-3 h-3" />
                  </div>
                </th>
                <th className="py-3 px-4">Δ vs Normal</th>
                <th 
                  className="py-3 px-4 cursor-pointer hover:text-white"
                  onClick={() => handleSort('sample_size_saturation_index_pct')}
                >
                  <div className="flex items-center gap-1">
                    SSSI % <ArrowUpDown className="w-3 h-3" />
                  </div>
                </th>
                <th className="py-3 px-4">95% Bootstrap CI</th>
                <th className="py-3 px-4 text-center">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-white/5 text-xs">
              {loading ? (
                <tr>
                  <td colSpan={10} className="py-12 text-center text-gray-400">
                    <div className="inline-block animate-spin rounded-full h-6 w-6 border-b-2 border-[#EB107E]"></div>
                    <div className="mt-2 text-xs">Loading audited batting records...</div>
                  </td>
                </tr>
              ) : batters.length === 0 ? (
                <tr>
                  <td colSpan={10} className="py-12 text-center text-gray-400">
                    No matching batters found for the specified filters.
                  </td>
                </tr>
              ) : (
                batters.map((b) => (
                  <tr 
                    key={b.player_id}
                    className="hover:bg-[#122131]/60 transition-colors group"
                  >
                    <td className="py-3.5 px-4 text-center">
                      <span className={`inline-flex items-center justify-center w-6 h-6 rounded-full font-mono text-xs font-bold ${
                        b.rank === 1 ? 'bg-[#EB107E] text-white shadow-md shadow-[#EB107E]/30' :
                        b.rank === 2 ? 'bg-[#FABC4D] text-[#051424] font-extrabold' :
                        b.rank === 3 ? 'bg-[#7BD0FF] text-[#051424] font-extrabold' :
                        'bg-white/5 text-gray-400'
                      }`}>
                        {b.rank}
                      </span>
                    </td>
                    <td className="py-3.5 px-4">
                      <div className="font-bold text-white group-hover:text-[#EB107E] transition-colors">
                        {b.player_name}
                      </div>
                      <div className="text-[11px] text-gray-400">{b.batting_role} · {b.team}</div>
                    </td>
                    <td className="py-3.5 px-4 font-mono font-extrabold text-[#EB107E] text-sm">
                      {b.bpri_score.toFixed(2)}
                    </td>
                    <td className="py-3.5 px-4 font-mono font-semibold text-white">
                      {b.pressure_strike_rate.toFixed(1)}
                    </td>
                    <td className="py-3.5 px-4 font-mono text-gray-300">
                      {b.pressure_batting_avg.toFixed(1)}
                    </td>
                    <td className="py-3.5 px-4 font-mono font-semibold text-[#FABC4D]">
                      {b.death_strike_rate.toFixed(1)}
                    </td>
                    <td className="py-3.5 px-4 font-mono">
                      <span className={b.delta_strike_rate_vs_normal >= 0 ? 'text-emerald-400' : 'text-red-400'}>
                        {b.delta_strike_rate_vs_normal >= 0 ? '+' : ''}{b.delta_strike_rate_vs_normal.toFixed(1)}
                      </span>
                    </td>
                    <td className="py-3.5 px-4">
                      <div className="flex items-center gap-2">
                        <span className="font-mono text-white text-xs">{b.sample_size_saturation_index_pct.toFixed(0)}%</span>
                        <div className="w-12 bg-white/10 h-1.5 rounded-full overflow-hidden">
                          <div 
                            className="bg-[#7BD0FF] h-full rounded-full"
                            style={{ width: `${Math.min(100, b.sample_size_saturation_index_pct)}%` }}
                          ></div>
                        </div>
                      </div>
                    </td>
                    <td className="py-3.5 px-4 font-mono text-[11px] text-gray-300">
                      [{b.bootstrap_95_ci_lower_sr.toFixed(1)}, {b.bootstrap_95_ci_upper_sr.toFixed(1)}]
                    </td>
                    <td className="py-3.5 px-4 text-center">
                      <button
                        onClick={() => navigate(`/profiles?id=${b.player_id}`)}
                        className="px-2.5 py-1 rounded bg-[#1C2B3C] hover:bg-[#EB107E] text-white text-[11px] font-semibold transition-all flex items-center gap-1 mx-auto"
                      >
                        Profile <ChevronRight className="w-3 h-3" />
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Uncertainty Notice Box */}
      <div className="bg-[#051424] border border-white/10 rounded-xl p-4 flex items-start gap-3 text-xs text-gray-400">
        <Info className="w-5 h-5 text-[#FABC4D] shrink-0 mt-0.5" />
        <div>
          <span className="font-bold text-white">Statistical Integrity Note: </span>
          <span className="text-[#FABC4D]">SSSI %</span> measures empirical sample size saturation relative to the Bayesian shrinkage threshold (K=60 balls). 
          The <span className="text-[#7BD0FF]">95% Bootstrap Confidence Interval</span> quantifies historical estimation uncertainty, NOT the probability of a batter succeeding in a future match.
        </div>
      </div>
    </div>
  );
};

