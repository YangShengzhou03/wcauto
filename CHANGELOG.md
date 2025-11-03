# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- 添加 `pyproject.toml` 配置文件，支持现代 Python 包管理
- 创建 `requirements-dev.txt` 文件，分离开发依赖
- 优化 `requirements.txt` 文件结构，添加版本锁定
- 改进 `README.md` 文档结构，添加英文版本支持
- 添加 `CHANGELOG.md` 文件记录版本变更
- 添加项目徽章和状态指示器
- 增强快速开始指南，添加多种安装方式

### Changed
- 更新依赖版本到最新稳定版本
- 改进文档结构和可读性
- 优化项目配置和构建流程

### Fixed
- 修复文档中的拼写错误和格式问题

## [1.0.0] - 2024-01-01

### Added
- 初始版本发布
- 基础微信自动化功能
- 支持消息发送、联系人管理、文件传输等核心功能
- 完整的 API 文档和示例代码

### Core Features
- 微信窗口检测和控制
- 消息发送和接收模拟
- 联系人列表管理
- 文件传输功能
- 群聊管理支持

## [0.1.0] - 2023-12-01

### Added
- 项目初始提交
- 基础自动化框架
- 核心功能模块
- 测试用例和文档

---

## Versioning Guidelines

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality in a backward compatible manner
- **PATCH** version for backward compatible bug fixes

## Release Process

1. Update version number in `pyproject.toml`
2. Update this changelog with release notes
3. Create a git tag for the release
4. Build and publish the package
5. Update documentation if needed

## Contributing

When contributing to this project, please add entries to this changelog for any significant changes:

- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for removed features
- **Fixed** for any bug fixes
- **Security** in case of vulnerabilities

## Links

- [GitHub Repository](https://github.com/YangShengzhou03/wcauto)
- [Documentation](https://github.com/YangShengzhou03/wcauto#readme)
- [Issue Tracker](https://github.com/YangShengzhou03/wcauto/issues)